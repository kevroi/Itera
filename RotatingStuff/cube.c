#include <stdio.h>
#include <math.h>
#include <string.h>
#include <unistd.h>

/*
 * Need to evaluate:
 * R_z * R_y * R_x * point
 * [ cos(theta_z) -sin(theta_z) 0 ]   [  cos(theta_y) 0 sin(theta_y) ]   [ 1      0             0       ]   [x]
 * [ sin(theta_z)  cos(theta_z) 0 ] * [       0       1      0       ] * [ 0 cos(theta_x) -sin(theta_x) ] * [y] 
 * [      0             0       1 ]   [ -sin(theta_y) 0 cos(theta_y) ]   [ 0 sin(theta_x)  cos(theta_x) ]   [z]
 */

float A, B, C;
float x, y, z;
float reciprocal_z;
int x_pixel, y_pixel;
int idx;

float cubeWidth = 10;
int width = 160, height = 44;
int cameraDistance = 60;
float zBuffer[160*44];
char buffer[160*44];
int bgASCIIcode = ' ';
float incrementSpeed = 0.6;
float K1 = 40;


float calculateX(int i, int j, int k){
    return j*sin(A)*sin(B)*cos(C) - k*cos(A)*sin(B)*cos(C) + j*cos(A)*sin(C) + k*sin(A)*sin(C) + i*cos(B)*cos(C);
}

float calculateY(int i, int j, int k){
    return j*cos(A)*cos(C) + k*sin(A)*cos(C) - j*sin(A)*sin(B)*sin(C) + k*cos(A)*sin(B)*sin(C) - i*cos(B)*sin(C);
}

float calculateZ(int i, int j, int k){
    return k*cos(A)*cos(B) - j*sin(A)*cos(B) + i*sin(B);
}

void calculateForSurface(float cubeX, float cubeY, float cubeZ, int ch) {
    x = calculateX(cubeX, cubeY, cubeZ);
    y = calculateY(cubeX, cubeY, cubeZ);
    z = calculateZ(cubeX, cubeY, cubeZ) + cameraDistance;
    
    reciprocal_z = 1/z;
    x_pixel = (int)(width/2 + K1*reciprocal_z*x*2);
    y_pixel = (int)(height/2 + K1*reciprocal_z*y);
    
    idx = x_pixel + y_pixel*width;
    if (idx>=0 && idx<width*height) {
        if (reciprocal_z > zBuffer[idx]){
            zBuffer[idx] = reciprocal_z;
            buffer[idx] = ch;
        }
    }
}

int main() {
    printf("\x1b[2J"); // clear screen

    while (1) {
        // set first width*height bytes of buffer to background
        memset(buffer, bgASCIIcode, width*height);
        // set first width*height*4 bytes of zBuffer to 0
        memset(zBuffer, 0, width*height*4);

        for (float cubeX = -cubeWidth; cubeX < cubeWidth; cubeX += incrementSpeed) {
            for (float cubeY = -cubeWidth; cubeY < cubeWidth; cubeY += incrementSpeed) {
                calculateForSurface(cubeX, cubeY, -cubeWidth, '$');
            }
        }
        printf("\x1b[H");

        for (int k = 0; k < width*height; k++) {
            putchar(k % width ? buffer[k] : 10); // put buffer[k] if k%width, else put 10
        }

        A += 0.005;
        B += 0.005;
        usleep(1000);
    }
    return 0;
}