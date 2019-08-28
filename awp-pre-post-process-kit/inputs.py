# 前处理输出目录
PREPROC_OUTPUT_DIR = "./awp"


# crust1.0提取的输入
# crust1.0目录
CRUST1_0_DIR = "./crust1.0"
# 划定提取区域（左上角及右下角坐标）
lat1 = 41.161831
lat2 = 39.361475
lon1 = 115.178618
lon2 = 117.512967
# 经纬+深度方向的格点数
xlati = 64
ylong = 64
zdepth = 64


# 震源的输入
# 震中 39.8 116.8
# from https://wenku.baidu.com/view/aeef9bfc04a1b0717fd5dd03.html?qq-pf-to=pcqq.c2c
# 39.8 116.8
HypocenterLong = 116.79
HypocenterLati = 39.77
HypocenterDepth = 12
# 震级？ Mw7.9
M0 = 8.97*pow(10,27-7)
# 震源断层面 走向 120，倾角 71，滑动角 90
strike = 120
dip = 71
rake = 90


# 可视化的输入
path_input = ''
input_filename_prefix = 'SX00'
input_filename_suffix = ['00500']

path_output = ''
output_filename_prefix = 'awp'

start_step = 100
stop_step = 1000
write_step = 500
n_ti_skp = 1
dt = 0.02 # second
xt = 500
yt = 500
zt = write_step
