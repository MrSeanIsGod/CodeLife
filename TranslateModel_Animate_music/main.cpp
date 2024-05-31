#include <opencv/highgui.h> ///使用 OpenCV 2.1 比較簡單, 只要用 High GUI 即可
#include <opencv/cv.h>
#include <GL/glut.h>
#include "CMP3_MCI.h"
CMP3_MCI myMP3;

int myTexture(char * filename)
{
    IplImage * img = cvLoadImage(filename); ///OpenCV讀圖
    cvCvtColor(img,img, CV_BGR2RGB); ///OpenCV轉色彩 (需要cv.h)
    glEnable(GL_TEXTURE_2D); ///1. 開啟貼圖功能
    GLuint id; ///準備一個 unsigned int 整數, 叫 貼圖ID
    glGenTextures(1, &id); /// 產生Generate 貼圖ID
    glBindTexture(GL_TEXTURE_2D, id); ///綁定bind 貼圖ID
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT); /// 貼圖參數, 超過包裝的範圖T, 就重覆貼圖
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT); /// 貼圖參數, 超過包裝的範圖S, 就重覆貼圖
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST); /// 貼圖參數, 放大時的內插, 用最近點
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST); /// 貼圖參數, 縮小時的內插, 用最近點
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img->width, img->height, 0, GL_RGB, GL_UNSIGNED_BYTE, img->imageData);
    return id;
}
#include <GL/glut.h>
#include "glm.h"
GLMmodel * Head = NULL; ///加的程式，有顆指標，指到模型檔
GLMmodel * LeftHand = NULL;
GLMmodel * LeftUpper = NULL;
GLMmodel * RightHand = NULL;
GLMmodel * RightUpper = NULL;
GLMmodel * Body = NULL;
GLMmodel * LeftLeg = NULL;
GLMmodel * RightLeg = NULL;
GLMmodel * LeftFoot = NULL;
GLMmodel * RightFoot = NULL;

void drawHead(void)
{
    if (!Head) {
        Head = glmReadOBJ("Head.obj"); // 將 "Head.obj" 改為 const char*
        if (!Head) exit(0);
        glmUnitize(Head);
        glmFacetNormals(Head);
        glmVertexNormals(Head, 90.0);
    }
    glmDraw(Head, GLM_SMOOTH | GLM_TEXTURE);
}

void drawLeftHand(void)
{
    if(!LeftHand){
        LeftHand = glmReadOBJ("LeftHand.obj");
        if(!LeftHand) exit(0);
        glmUnitize(LeftHand);
        glmFacetNormals(LeftHand);
        glmVertexNormals(LeftHand, 90.0);
    }
    glmDraw(LeftHand, GLM_SMOOTH | GLM_TEXTURE);
}

void drawLeftUpper(void)
{
    if(!LeftUpper){
        LeftUpper = glmReadOBJ("LeftUpper.obj");
        if(!LeftUpper) exit(0);
        glmUnitize(LeftUpper);
        glmFacetNormals(LeftUpper);
        glmVertexNormals(LeftUpper, 90.0);
    }
    glmDraw(LeftUpper, GLM_SMOOTH | GLM_TEXTURE);
}

void drawRightHand(void)
{
    if(!RightHand){
        RightHand = glmReadOBJ("RightHand.obj");
        if(!RightHand) exit(0);
        glmUnitize(RightHand);
        glmFacetNormals(RightHand);
        glmVertexNormals(RightHand, 90.0);
    }
    glmDraw(RightHand, GLM_SMOOTH | GLM_TEXTURE);
}

void drawRightUpper(void)
{
    if(!RightUpper){
        RightUpper = glmReadOBJ("RightUpper.obj");
        if(!RightUpper) exit(0);
        glmUnitize(RightUpper);
        glmFacetNormals(RightUpper);
        glmVertexNormals(RightUpper, 90.0);
    }
    glmDraw(RightUpper, GLM_SMOOTH | GLM_TEXTURE);
}

void drawBody(void)
{
    if(!Body){
        Body = glmReadOBJ("Body.obj");
        if(!Body) exit(0);
        glmUnitize(Body);
        glmFacetNormals(Body);
        glmVertexNormals(Body, 90.0);
    }
    glmDraw(Body, GLM_SMOOTH | GLM_TEXTURE);
}

void drawLeftLeg(void)
{
    if(!LeftLeg){
        LeftLeg = glmReadOBJ("LeftLeg.obj");
        if(!LeftLeg) exit(0);
        glmUnitize(LeftLeg);
        glmFacetNormals(LeftLeg);
        glmVertexNormals(LeftLeg, 90.0);
    }
    glmDraw(LeftLeg, GLM_SMOOTH | GLM_TEXTURE);
}

void drawRightLeg(void)
{
    if(!RightLeg){
        RightLeg = glmReadOBJ("RightLeg.obj");
        if(!RightLeg) exit(0);
        glmUnitize(RightLeg);
        glmFacetNormals(RightLeg);
        glmVertexNormals(RightLeg, 90.0);
    }
    glmDraw(RightLeg, GLM_SMOOTH | GLM_TEXTURE);
}

void drawLeftFoot(void)
{
    if(!LeftFoot){
        LeftFoot = glmReadOBJ("LeftFoot.obj");
        if(!LeftFoot) exit(0);
        glmUnitize(LeftFoot);
        glmFacetNormals(LeftFoot);
        glmVertexNormals(LeftFoot, 90.0);
    }
    glmDraw(LeftFoot, GLM_SMOOTH | GLM_TEXTURE);
}

void drawRightFoot(void)
{
    if(!RightFoot){
        RightFoot = glmReadOBJ("RightFoot.obj");
        if(!RightFoot) exit(0);
        glmUnitize(RightFoot);
        glmFacetNormals(RightFoot);
        glmVertexNormals(RightFoot, 90.0);
    }
    glmDraw(RightFoot, GLM_SMOOTH | GLM_TEXTURE);
}

int angleID = 0;
float angleX[10] = { }; ///float angle=0, da=-1;
float angleY[10] = { };
void display()
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glPushMatrix();
        glRotatef(180,0,1,0);
        glRotatef(angleX[0], 1, 0, 0);
        glRotatef(angleY[0], 0, 1, 0);
        drawBody();

        glPushMatrix();
            glTranslatef(0.12, 0.13, 0);
            glRotatef(angleX[1], 1, 0, 0);
            glRotatef(angleY[1], 0, 1, 0);
            glTranslatef(0.08, -0.05, 0);
            drawLeftUpper();
            glPushMatrix();
                glTranslatef(0.05, -0.08, 0); ///(3)掛到肩上
                glRotatef(angleX[2], 1, 0, 0); ///(2)轉動
                glRotatef(angleY[2], 0, 1, 0);
                glTranslatef(0.1, -0.1, 0.05); ///(1)把旋轉中心，放正中心
                drawLeftHand(); ///glutSolidTeapot( 0.3 );
            glPopMatrix();
        glPopMatrix();

        glPushMatrix();
            glTranslatef(-0.1, 0.13, 0);
            glRotatef(angleX[3], 1, 0, 0); ///(2)轉動
            glRotatef(angleY[3], 0, 1, 0);
            glTranslatef(-0.08, -0.05, 0);
            drawRightUpper();
            glPushMatrix();
                glTranslatef(-0.04, -0.03, 0.02); ///(3)掛到肩上
                glRotatef(angleX[4], 1, 0, 0); ///(2)轉動
                glRotatef(angleY[4], 0, 1, 0);
                glTranslatef(-0.15, -0.13, 0.05); ///(1)把旋轉中心，放正中心
                drawRightHand(); ///glutSolidTeapot( 0.3 );
            glPopMatrix();
        glPopMatrix();

        glPushMatrix();
            //glRotatef(180,0,1,0);
            glTranslatef(0, 0.24, -0.05); ///(3)掛到肩上
            glRotatef(angleX[5], 1, 0, 0); ///(2)轉動
            glRotatef(angleY[5], 0, 1, 0);
            glTranslatef(0, 0.05, 0.03); ///(1)把旋轉中心，放正中心
            drawHead(); ///glutSolidTeapot( 0.3 );
        glPopMatrix();

        glPushMatrix();
            glScalef(0.5,0.5,0.5);
            glTranslatef(0.12, -0.5, 0);
            glRotatef(angleX[6], 1, 0, 0);
            glRotatef(angleY[6], 0, 1, 0);
            glTranslatef(0, -0.2, 0);
            drawLeftLeg();
            glPushMatrix();
                glScalef(0.4,0.4,0.4);
                glTranslatef(0.05, -0.5, 0); ///(3)掛到肩上
                glRotatef(angleX[7], 1, 0, 0); ///(2)轉動
                glRotatef(angleY[7], 0, 1, 0);
                glTranslatef(0, -1, 0.2); ///(1)把旋轉中心，放正中心
                drawLeftFoot(); ///glutSolidTeapot( 0.3 );
            glPopMatrix();
        glPopMatrix();

        glPushMatrix();
            glScalef(0.5,0.5,0.5);
            glTranslatef(-0.1, -0.5, 0);
            glRotatef(angleX[8], 1, 0, 0); ///(2)轉動
            glRotatef(angleY[8], 0, 1, 0);
            glTranslatef(0, -0.2, 0);
            drawRightLeg();
            glPushMatrix();
                glScalef(0.4,0.4,0.4);
                glTranslatef(-0.04, -0.5, 0.02); ///(3)掛到肩上
                glRotatef(angleX[9], 1, 0, 0); ///(2)轉動
                glRotatef(angleY[9], 0, 1, 0);
                glTranslatef(0, -1, 0.2); ///(1)把旋轉中心，放正中心
                drawRightFoot(); ///glutSolidTeapot( 0.3 );
            glPopMatrix();
        glPopMatrix();

    glPopMatrix();
    glutSwapBuffers();
}

const GLfloat light_ambient[]  = { 0.0f, 0.0f, 0.0f, 1.0f };
const GLfloat light_diffuse[]  = { 1.0f, 1.0f, 1.0f, 1.0f };
const GLfloat light_specular[] = { 1.0f, 1.0f, 1.0f, 1.0f };
const GLfloat light_position[] = { 2.0f, 5.0f, -5.0f, 0.0f };

const GLfloat mat_ambient[]    = { 0.7f, 0.7f, 0.7f, 1.0f };
const GLfloat mat_diffuse[]    = { 0.8f, 0.8f, 0.8f, 1.0f };
const GLfloat mat_specular[]   = { 1.0f, 1.0f, 1.0f, 1.0f };
const GLfloat high_shininess[] = { 100.0f };

#include <stdio.h>
FILE * fout = NULL;
FILE * fin = NULL;

void timer(int t);

void keyboard(unsigned char key, int x, int y) {
    if(key=='p'){
        glutTimerFunc(0,timer,0);
        myMP3.Load("18.wav");
        myMP3.Play();
    }
    if(key=='r') {
        if(fin==NULL) fin = fopen("angle.txt", "r");
        for(int i=0; i<10; i++) {
            fscanf(fin, "%f", & angleX[i] );
            fscanf(fin, "%f", & angleY[i] );
        }
        glutPostRedisplay();
    }

    if(key=='s') {
        if(fout==NULL) fout = fopen("angle.txt", "w+");
        for(int i=0; i<10; i++) {
            printf("%.1f ", angleX[i] );
            fprintf(fout, "%.1f ", angleX[i] );
            printf("%.1f ", angleY[i] );
            fprintf(fout, "%.1f ", angleY[i] );
        }
        printf("\n");
        fprintf(fout, "\n");
    }
    if(key=='0') angleID = 0;
    if(key=='1') angleID = 1;
    if(key=='2') angleID = 2;
    if(key=='3') angleID = 3;
    if(key=='4') angleID = 4;
    if(key=='5') angleID = 5;
    if(key=='6') angleID = 6;
    if(key=='7') angleID = 7;
    if(key=='8') angleID = 8;
    if(key=='9') angleID = 9;
}
int oldX = 0, oldY = 0;
void mouse(int button, int state, int x, int y) {
    oldX = x;
    oldY = y;
}

void motion(int x, int y) {
    angleX[angleID] += y - oldY; ///angle[angleID] = y;
    angleY[angleID] += x - oldX;
    oldX = x;
    oldY = y;
    glutPostRedisplay(); ///貼上便利貼,提醒GLUT要重畫畫面
}
float oldAngleX[10]={};
float oldAngleY[10]={};
float newAngleX[10]={};
float newAngleY[10]={};
void timer(int t){
    glutTimerFunc(50,timer,t+1);
    if(fin==NULL) fin=fopen("angle.txt","r");
    if(t%20==0){
        for(int i=0;i<10;i++){
            oldAngleX[i]=newAngleX[i];
            oldAngleY[i]=newAngleY[i];
            fscanf(fin,"%f",&newAngleX[i]);
            fscanf(fin,"%f",&newAngleY[i]);
        }
    }
    float alpha=(t%20)/20.0;
    for(int i=0;i<10;i++){
        angleX[i]=alpha*newAngleX[i]+(1-alpha)*oldAngleX[i];
        angleY[i]=alpha*newAngleY[i]+(1-alpha)*oldAngleY[i];
    }
    glutPostRedisplay();
    printf("你呼叫了 timer(%d)\n",t);
}



int main(int argc, char* argv[])
{
    printf("程式開始執行\n");
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH);
    glutCreateWindow("TranslateModel_Animate_music");
    glutDisplayFunc(display);
    glutIdleFunc(display); ///加入旋轉
    glutKeyboardFunc(keyboard);
    glutMouseFunc(mouse);
    glutMotionFunc(motion);

    myTexture("texture.jpg");

    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LESS);

    glEnable(GL_LIGHT0);
    glEnable(GL_NORMALIZE);
    glEnable(GL_COLOR_MATERIAL);
    glEnable(GL_LIGHTING);

    glLightfv(GL_LIGHT0, GL_AMBIENT,  light_ambient);
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  light_diffuse);
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular);
    glLightfv(GL_LIGHT0, GL_POSITION, light_position);

    glMaterialfv(GL_FRONT, GL_AMBIENT,   mat_ambient);
    glMaterialfv(GL_FRONT, GL_DIFFUSE,   mat_diffuse);
    glMaterialfv(GL_FRONT, GL_SPECULAR,  mat_specular);
    glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess);


    glutMainLoop();
}
