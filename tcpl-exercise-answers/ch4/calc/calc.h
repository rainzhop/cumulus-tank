#define NUMBER '0'
#define SIN 0x100
#define EXP 0x101
#define POW 0x102
#define ANS 0x103
#define UNKNOWN 0x104

int getop(char [], char[]);

int getch(void);
void ungetch(int);

void push(double);
double pop(void);

void print_top(void);
double copy_top(void);
void swap_top(void);
void clear(void);
