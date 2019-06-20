/*
 * pngseg.c
 *
 *  Created on: 2019年6月19日
 *      Author: ec
 */

#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#include "png.h"

typedef struct _pngfile_
{
	FILE *fp;
	png_structp png_ptr;
	png_infop info_ptr;
} pngfile;

// info on input png file
png_uint_32 width, height;
int bit_depth, color_type, interlace_method, compression_method, filter_method;
pngfile in_file;

// info on output png files
png_uint_32 out_width, out_height;
png_uint_32 out_width_remain, out_height_remain; // width and height of rightest or lowest outpng
int n_x, n_y;
pngfile *out_files;

void outpng_close()
{
	for (int i = 0; i < n_x; ++i)
	{
		if (out_files[i].fp == NULL) continue;
		else fclose(out_files[i].fp);
		png_destroy_info_struct(out_files[i].png_ptr, &out_files[i].info_ptr);
	}
	return;
}

void outpng_create(int index_y)
{
	for (int i = 0; i < n_x; ++i)
	{
		char file_name[128] = {0, };
		sprintf(file_name, "Y%d_X%d.png", index_y, i);
		out_files[i].fp = fopen(file_name, "wb");

		out_files[i].png_ptr = png_create_write_struct(PNG_LIBPNG_VER_STRING, NULL, NULL, NULL);
        if (!out_files[i].png_ptr)
        	fprintf(stderr, "outpng_create png_create_write_struct failed");

        out_files[i].info_ptr = png_create_info_struct(out_files[i].png_ptr);
        if (!out_files[i].info_ptr)
        	fprintf(stderr, "outpng_create png_create_info_struct failed");

        png_init_io(out_files[i].png_ptr, out_files[i].fp);

        png_uint_32 w, h;
        if (i == n_x - 1 && i != 0) w = out_width_remain;
        else w = out_width;

        if (index_y == n_y - 1 && index_y != 0) h = out_height_remain;
        else h = out_height;

        png_set_IHDR(out_files[i].png_ptr, out_files[i].info_ptr, w, h,
                     bit_depth, color_type, PNG_INTERLACE_NONE,
                     PNG_COMPRESSION_TYPE_BASE, PNG_FILTER_TYPE_BASE);

        png_write_info(out_files[i].png_ptr, out_files[i].info_ptr);
	}
	return;
}

void pngseg_outpng_init()
{
	// number of segmentation on x axis
	n_x = width / out_width;
	out_width_remain = width % out_width;
	if (out_width_remain != 0) n_x++;

	// number of segmentation on y axis
	n_y = height / out_height;
	out_height_remain = height % out_height;
	if (out_height_remain != 0) n_y++;

	printf("--------- input png ---------\n");
	printf("width = %d, height = %d\n", width, height);
	printf("out_width = %d, out_height = %d\n", out_width, out_height);
	printf("out n_x = %d, n_y = %d\n", n_x, n_y);
	printf("-----------------------------\n");

	out_files = (pngfile *)malloc(n_x * sizeof(pngfile));

	return;
}

void pngseg_write_out_row(int n_x, png_bytep row)
{
	int out_row_size = sizeof(png_byte) * out_width * 3;
	png_bytep p = row;
	int i;
	for (i = 0; i < n_x - 1; ++i)
	{
		png_bytep out_row = (png_bytep)malloc(out_row_size);
		memcpy(out_row, p, out_row_size);
		png_write_row(out_files[i].png_ptr, out_row);
		p += out_row_size;
		free(out_row);
	}
	if (i == 0) // only one image on horizontal
		out_row_size = sizeof(png_byte) * out_width * 3;
	else // the last one on horizontal
		out_row_size = sizeof(png_byte) * out_width_remain * 3;
	png_bytep out_row = (png_bytep)malloc(out_row_size);
	memcpy(out_row, p, out_row_size);
	png_write_row(out_files[i].png_ptr, out_row);
	free(out_row);
	return;
}

void pngseg_write_out_end()
{
	for (int i = 0; i < n_x; ++i)
	{
		png_write_end(out_files[i].png_ptr, NULL);
	}
	return;
}

void pngseg_do_seg()
{
	pngseg_outpng_init();
	int index_y = 0, row_id = 0;

	png_start_read_image(in_file.png_ptr);
	png_bytep row;
	row = png_malloc(in_file.png_ptr, png_get_rowbytes(in_file.png_ptr, in_file.info_ptr));
	while (row_id < height)
	{
		png_read_row(in_file.png_ptr, row, NULL);
		if (row_id % out_height == 0)
		{
			if (row_id != 0) // not first row in inpng
			{
				printf("Y = %d, output (%d/%d) files done...\n", index_y, n_x*index_y, n_x*n_y);
				pngseg_write_out_end();
				outpng_close();
			}
			outpng_create(index_y);
			index_y++;
		}

		pngseg_write_out_row(n_x, row);
		row_id++;
	}

	printf("Y = %d, output (%d/%d) files done...\n", index_y, n_x*index_y, n_x*n_y);
	pngseg_write_out_end();
	outpng_close();

	png_free(in_file.png_ptr, row);
	png_destroy_info_struct(in_file.png_ptr, &in_file.info_ptr);
	return;
}

void pngseg_inpng_init(const char *file_name)
{
	in_file.fp = fopen(file_name, "rb");
	if (in_file.fp == NULL)
	{
		perror("file open error: ");
		exit(-1);
	}

	in_file.png_ptr = png_create_read_struct(PNG_LIBPNG_VER_STRING,
			NULL, NULL, NULL);
	if (in_file.png_ptr == NULL)
	{
		fprintf(stderr, "out of memory allocating png_struct\n");
		exit(-1);
	}

	in_file.info_ptr = png_create_info_struct(in_file.png_ptr);
	if (in_file.info_ptr == NULL)
	{
		fprintf(stderr, "out of memory allocating png_info\n");
		exit(-1);
	}

	png_init_io(in_file.png_ptr, in_file.fp);
	png_read_info(in_file.png_ptr, in_file.info_ptr);

	int ret = png_get_IHDR(in_file.png_ptr, in_file.info_ptr, &width, &height,
			&bit_depth, &color_type, &interlace_method,
			&compression_method, &filter_method);
	if (ret == 0)
	{
		fprintf(stderr, "png_get_IHDR error\n");
		exit(-1);
	}

	if (out_width == 0) out_width = width;
	if (out_height == 0) out_height = height;

	if (interlace_method != PNG_INTERLACE_NONE)
	{
		fprintf(stderr, "only support interlace = NONE...\n");
		exit(-1);
	}

	ret = png_get_color_type(in_file.png_ptr, in_file.info_ptr);
	if (ret != PNG_COLOR_TYPE_RGB)
	{
		fprintf(stderr, "only support color type = RGB...\n");
		exit(-1);
	}
}

int main(int argc, const char **argv)
{
	const char *filename = NULL;
	if (argc == 4)
	{
		filename = argv[1];
		out_width = atoi(argv[2]);
		out_height = atoi(argv[3]);
	}
	else
	{
		printf("usage: pngseg <filename> <out_width> <out_height>\n"
			   "    if out_width or out_height is set to 0, it means that the input \n"
			   "  file will be segmented vertically or horizontally. out_width and \n"
			   "  out_height should not be set to 0 at the same time. \n");
		exit(-1);
	}

	pngseg_inpng_init(filename);
	pngseg_do_seg();

	return 0;
}
