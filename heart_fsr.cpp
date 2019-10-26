#define BAUDRATE B9600
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <termios.h>
#include <unistd.h>

#include <time.h>
#include <sys/time.h>

#define LIMIT 180

int serial_ardinoread(char *,char *);

void readserial(int fairu,short meron[2]);
	
int main(int argc,char *argv[])
{
  printf("limit is %d\n",LIMIT);
	char devicename[255];// = "/dev/ttyACM1";
  sprintf(devicename,"%s",argv[1]);

	printf("devname%s\n",devicename);
	serial_ardinoread(devicename,"name");
}

void readserial(int fairu,short meron[2]){
	short ringo[1];
	int i=0;
	while(i<2){
		if(read(fairu,ringo,1)!=0){
			meron[i]=ringo[0];
//			printf("meron[%d]=%d\n",i,meron[i]);
			i++;
		}
	}
}

int serial_ardinoread(char *devicename,char *messege)
{
	char buf[1];
	short short_buf_a[2], short_buf_b[2],pressure, heart;
	int val;
	int flg,fd,len;

	struct termios oldtio,newtio;

	fd = open(devicename,O_RDWR|O_NONBLOCK); //デバイスのオープン
	if(fd<0) //デバイスのオープンに失敗した場合
	{
		printf("ERROR on device open.\n");
		exit(1);
	}

  struct timeval nowTime;
	time_t timer;
  time_t start_time;
	struct tm *t_st = localtime(&timer);

  int t;
  int test_t;

	ioctl(fd,TCGETS,&oldtio);//現状のシリアルポート設定を退避
	newtio = oldtio;
	newtio.c_cflag = BAUDRATE | CRTSCTS | CS8 | CLOCAL | CREAD;

	ioctl(fd,TCSETS,&newtio);
	flg =1;
//	strcpy(mes,"");

  FILE *heartfile;
  heartfile = fopen("/home/kazumi/mogura/heart_out.csv","w");
  gettimeofday(&nowTime,NULL);
  time(&timer);
  time(&start_time);

  if(heartfile==NULL){
    printf("cannot open file\n");
  }else{
    while(flg){

        gettimeofday(&nowTime,NULL);
        time(&timer);
        t_st = localtime(&timer);
        double t=difftime(timer,start_time);

        if(t>LIMIT){
          break;
        }else{
          len=read(fd,buf,1);
          if(len==0)
          {
            continue;
          }
          else if(len<0)//IOエラー
          {
          //  printf("out\n");
          //	exit(2);
          }
          else if(buf[0]=='H'){
            readserial(fd,short_buf_a);
            readserial(fd,short_buf_b);
            heart= short_buf_a[0]<<8|(short_buf_a[1]&0x00ff);
            pressure = short_buf_b[0]<<8|(short_buf_b[1]&0x00ff);
            //meron = (short_buf[0]<<8&0x00ff)|(short_buf[1]&0x00ff);
            //8bit shift && high 8bit mask/
            fprintf(heartfile,"%d,%d,%02d%02d,%02d,%02d,%02d.%02d\n",pressure,heart,(int)t_st->tm_mon,(int)t_st->tm_mday,(int)t_st->tm_hour,(int)t_st->tm_min,(int)t_st->tm_sec,(int)nowTime.tv_usec);
            //printf("%d,%d\n",pressure,heart);
    //				val=meron+ringo;
          }
        }
    }
  }
	ioctl(fd,TCSETS,&oldtio);

  fclose(heartfile);
	close(fd);

	return 0;
}
