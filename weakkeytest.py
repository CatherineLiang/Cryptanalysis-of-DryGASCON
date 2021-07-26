# _*_ coding: utf-8 _*_
import os
import sys
import re
import subprocess
from time import sleep
import shutil
import random


def int2bin(n, count=5):
    """returns the binary of integer n, using count number of digits"""
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

def cvc(keyindex,trailindex):
    # generate cvc files
     
        fp = open( './'+str(keyindex)+'/'+str(trailindex)+'.cvc', 'a' )
        round = 4
        
        for i in range(0,4):
            fp.write("x_value_%d: BITVECTOR(32) ;\n" %(i) )
        fp.write("\n")
        
        fp.write("index: BITVECTOR(20) ;\n" )
        fp.write("\n")
        for r in range(0,round+1):
            fp.write("index1_%d: BITVECTOR(10) ;\n" %(r) )
        fp.write("\n")
        for r in range(0,round+1):
            fp.write("index2_%d: BITVECTOR(10) ;\n" %(r) )
        fp.write("\n")
        fp.write("ASSERT( index1_0 = index2_0 ) ;\n" )
        fp.write("ASSERT( index1_1 = index2_1 ) ;\n" )
        
        fp.write("ASSERT( index1_2 = 0bin0000000000 ) ;\n" )      
        fp.write("ASSERT( index1_3 = 0bin0000101000 ) ;\n" )
        fp.write("ASSERT( index1_4 = 0bin1101000010 ) ;\n" )
        
        fp.write("ASSERT( index2_2 = 0bin0001010100 ) ;\n" )      
        fp.write("ASSERT( index2_3 = 0bin1001000000 ) ;\n" )
        fp.write("ASSERT( index2_4 = 0bin0001000010 ) ;\n" )
        
        fp.write("ASSERT( index = index1_0@index1_1 ) ;\n" )
        fp.write("\n")
        
        for r in range(0,round+1):
            for i in range(0,5):
                fp.write("c_value_index1_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")
        for r in range(0,round+1):
            for i in range(0,5):
                fp.write("c_value_index2_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")        
        
        for r in range(0,round+1):
            for i in range(0,5):
                fp.write("afterxor_value_index1_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")
        
        for r in range(0,round):
            for i in range(0,5):
                fp.write("middlesbox_1_value_index1_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")      
        for r in range(0,round):
            for i in range(0,5):
                fp.write("middlesbox_2_value_index1_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")
        for r in range(0,round):
            for i in range(0,5):
                fp.write("middlesbox_3_value_index1_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")
        for r in range(0,round):
            for i in range(0,5):
                fp.write("middlesbox_4_value_index1_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")
        for r in range(0,round):
            for i in range(0,5):
                fp.write("aftersbox_value_index1_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")
        
        for r in range(0,round):
            for i in range(0,5):
                fp.write("middlelinearlayer_value_index1_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")    
        for r in range(0,round):
            for i in range(0,5):
                fp.write("afterlinearlayer_value_index1_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")        

        for r in range(0,round+1):
            fp.write("ASSERT( (index1_%d[1:0] = 0bin00) => (afterxor_value_index1_%d_0[31:0] = BVXOR(c_value_index1_%d_0[31:0],x_value_0)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[1:0] = 0bin01) => (afterxor_value_index1_%d_0[31:0] = BVXOR(c_value_index1_%d_0[31:0],x_value_1)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[1:0] = 0bin10) => (afterxor_value_index1_%d_0[31:0] = BVXOR(c_value_index1_%d_0[31:0],x_value_2)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[1:0] = 0bin11) => (afterxor_value_index1_%d_0[31:0] = BVXOR(c_value_index1_%d_0[31:0],x_value_3)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[3:2] = 0bin00) => (afterxor_value_index1_%d_1[31:0] = BVXOR(c_value_index1_%d_1[31:0],x_value_0)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[3:2] = 0bin01) => (afterxor_value_index1_%d_1[31:0] = BVXOR(c_value_index1_%d_1[31:0],x_value_1)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[3:2] = 0bin10) => (afterxor_value_index1_%d_1[31:0] = BVXOR(c_value_index1_%d_1[31:0],x_value_2)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[3:2] = 0bin11) => (afterxor_value_index1_%d_1[31:0] = BVXOR(c_value_index1_%d_1[31:0],x_value_3)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[5:4] = 0bin00) => (afterxor_value_index1_%d_2[31:0] = BVXOR(c_value_index1_%d_2[31:0],x_value_0)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[5:4] = 0bin01) => (afterxor_value_index1_%d_2[31:0] = BVXOR(c_value_index1_%d_2[31:0],x_value_1)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[5:4] = 0bin10) => (afterxor_value_index1_%d_2[31:0] = BVXOR(c_value_index1_%d_2[31:0],x_value_2)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[5:4] = 0bin11) => (afterxor_value_index1_%d_2[31:0] = BVXOR(c_value_index1_%d_2[31:0],x_value_3)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[7:6] = 0bin00) => (afterxor_value_index1_%d_3[31:0] = BVXOR(c_value_index1_%d_3[31:0],x_value_0)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[7:6] = 0bin01) => (afterxor_value_index1_%d_3[31:0] = BVXOR(c_value_index1_%d_3[31:0],x_value_1)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[7:6] = 0bin10) => (afterxor_value_index1_%d_3[31:0] = BVXOR(c_value_index1_%d_3[31:0],x_value_2)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[7:6] = 0bin11) => (afterxor_value_index1_%d_3[31:0] = BVXOR(c_value_index1_%d_3[31:0],x_value_3)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[9:8] = 0bin00) => (afterxor_value_index1_%d_4[31:0] = BVXOR(c_value_index1_%d_4[31:0],x_value_0)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[9:8] = 0bin01) => (afterxor_value_index1_%d_4[31:0] = BVXOR(c_value_index1_%d_4[31:0],x_value_1)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[9:8] = 0bin10) => (afterxor_value_index1_%d_4[31:0] = BVXOR(c_value_index1_%d_4[31:0],x_value_2)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index1_%d[9:8] = 0bin11) => (afterxor_value_index1_%d_4[31:0] = BVXOR(c_value_index1_%d_4[31:0],x_value_3)) ) ;\n" %(r,r,r) ) 
        fp.write("\n")       
        for r in range(0,round+1):
            for i in range(0,5):
                fp.write("ASSERT( afterxor_value_index1_%d_%d[63:32] = c_value_index1_%d_%d[63:32] ) ;\n" %(r,i,r,i) )
        fp.write("\n")
        
        for r in range(0,round):
            fp.write("ASSERT( middlesbox_1_value_index1_%d_0 = BVXOR(afterxor_value_index1_%d_0,afterxor_value_index1_%d_4) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_1_value_index1_%d_1 = afterxor_value_index1_%d_1 ) ;\n" %(r,r) )
            fp.write("ASSERT( middlesbox_1_value_index1_%d_2 = BVXOR(afterxor_value_index1_%d_2,afterxor_value_index1_%d_1) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_1_value_index1_%d_3 = afterxor_value_index1_%d_3 ) ;\n" %(r,r) )
            fp.write("ASSERT( middlesbox_1_value_index1_%d_4 = BVXOR(afterxor_value_index1_%d_4,afterxor_value_index1_%d_3) ) ;\n" %(r,r,r) )
        fp.write("\n") 
        for r in range(0,round):
            fp.write("ASSERT( middlesbox_2_value_index1_%d_0 = (~middlesbox_1_value_index1_%d_0) & middlesbox_1_value_index1_%d_1 ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_2_value_index1_%d_1 = (~middlesbox_1_value_index1_%d_1) & middlesbox_1_value_index1_%d_2 ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_2_value_index1_%d_2 = (~middlesbox_1_value_index1_%d_2) & middlesbox_1_value_index1_%d_3 ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_2_value_index1_%d_3 = (~middlesbox_1_value_index1_%d_3) & middlesbox_1_value_index1_%d_4 ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_2_value_index1_%d_4 = (~middlesbox_1_value_index1_%d_4) & middlesbox_1_value_index1_%d_0 ) ;\n" %(r,r,r) )
        fp.write("\n")       
        for r in range(0,round):
            fp.write("ASSERT( middlesbox_3_value_index1_%d_0 = BVXOR(middlesbox_1_value_index1_%d_0,middlesbox_2_value_index1_%d_1) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_3_value_index1_%d_1 = BVXOR(middlesbox_1_value_index1_%d_1,middlesbox_2_value_index1_%d_2) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_3_value_index1_%d_2 = BVXOR(middlesbox_1_value_index1_%d_2,middlesbox_2_value_index1_%d_3) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_3_value_index1_%d_3 = BVXOR(middlesbox_1_value_index1_%d_3,middlesbox_2_value_index1_%d_4) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_3_value_index1_%d_4 = BVXOR(middlesbox_1_value_index1_%d_4,middlesbox_2_value_index1_%d_0) ) ;\n" %(r,r,r) )
        fp.write("\n")       
        for r in range(0,round):
            fp.write("ASSERT( middlesbox_4_value_index1_%d_0 = BVXOR(middlesbox_3_value_index1_%d_0,middlesbox_3_value_index1_%d_4) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_4_value_index1_%d_1 = BVXOR(middlesbox_3_value_index1_%d_0,middlesbox_3_value_index1_%d_1) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_4_value_index1_%d_2 = middlesbox_3_value_index1_%d_2 ) ;\n" %(r,r) )
            fp.write("ASSERT( middlesbox_4_value_index1_%d_3 = BVXOR(middlesbox_3_value_index1_%d_2,middlesbox_3_value_index1_%d_3) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_4_value_index1_%d_4 = middlesbox_3_value_index1_%d_4 ) ;\n" %(r,r) )
        fp.write("\n")  
        for r in range(0,round):
            fp.write("ASSERT( aftersbox_value_index1_%d_0 = middlesbox_4_value_index1_%d_0 ) ;\n" %(r,r) )
            fp.write("ASSERT( aftersbox_value_index1_%d_1 = middlesbox_4_value_index1_%d_1 ) ;\n" %(r,r) )
            fp.write("ASSERT( aftersbox_value_index1_%d_2 = ~middlesbox_4_value_index1_%d_2 ) ;\n" %(r,r) )
            fp.write("ASSERT( aftersbox_value_index1_%d_3 = middlesbox_4_value_index1_%d_3 ) ;\n" %(r,r) )
            fp.write("ASSERT( aftersbox_value_index1_%d_4 = middlesbox_4_value_index1_%d_4 ) ;\n" %(r,r) )
        fp.write("\n")
        
        for r in range(0,round):
            fp.write("ASSERT( middlelinearlayer_value_index1_%d_0 = BVXOR(aftersbox_value_index1_%d_0,aftersbox_value_index1_%d_0[9:0]@aftersbox_value_index1_%d_0[31:10]@aftersbox_value_index1_%d_0[40:32]@aftersbox_value_index1_%d_0[63:41]) ) ;\n" %(r,r,r,r,r,r) )
            fp.write("ASSERT( afterlinearlayer_value_index1_%d_0 = BVXOR(middlelinearlayer_value_index1_%d_0,aftersbox_value_index1_%d_0[45:32]@aftersbox_value_index1_%d_0[63:46]@aftersbox_value_index1_%d_0[13:0]@aftersbox_value_index1_%d_0[31:14]) ) ;\n" %(r,r,r,r,r,r) )
        fp.write("\n")    
        for r in range(0,round):
            fp.write("ASSERT( middlelinearlayer_value_index1_%d_1 = BVXOR(aftersbox_value_index1_%d_1,aftersbox_value_index1_%d_1[30:0]@aftersbox_value_index1_%d_1[31:31]@aftersbox_value_index1_%d_1[61:32]@aftersbox_value_index1_%d_1[63:62]) ) ;\n" %(r,r,r,r,r,r) )
            fp.write("ASSERT( afterlinearlayer_value_index1_%d_1 = BVXOR(middlelinearlayer_value_index1_%d_1,aftersbox_value_index1_%d_1[50:32]@aftersbox_value_index1_%d_1[63:51]@aftersbox_value_index1_%d_1[18:0]@aftersbox_value_index1_%d_1[31:19]) ) ;\n" %(r,r,r,r,r,r) )
        fp.write("\n")      
        for r in range(0,round):
            fp.write("ASSERT( middlelinearlayer_value_index1_%d_2 = BVXOR(aftersbox_value_index1_%d_2,aftersbox_value_index1_%d_2[0:0]@aftersbox_value_index1_%d_2[31:1]@aftersbox_value_index1_%d_2[63:32]) ) ;\n" %(r,r,r,r,r) )
            fp.write("ASSERT( afterlinearlayer_value_index1_%d_2 = BVXOR(middlelinearlayer_value_index1_%d_2,aftersbox_value_index1_%d_2[34:32]@aftersbox_value_index1_%d_2[63:35]@aftersbox_value_index1_%d_2[2:0]@aftersbox_value_index1_%d_2[31:3]) ) ;\n" %(r,r,r,r,r,r) )
        fp.write("\n")
        for r in range(0,round):
            fp.write("ASSERT( middlelinearlayer_value_index1_%d_3 = BVXOR(aftersbox_value_index1_%d_3,aftersbox_value_index1_%d_3[36:32]@aftersbox_value_index1_%d_3[63:37]@aftersbox_value_index1_%d_3[4:0]@aftersbox_value_index1_%d_3[31:5]) ) ;\n" %(r,r,r,r,r,r) )
            fp.write("ASSERT( afterlinearlayer_value_index1_%d_3 = BVXOR(middlelinearlayer_value_index1_%d_3,aftersbox_value_index1_%d_3[8:0]@aftersbox_value_index1_%d_3[31:9]@aftersbox_value_index1_%d_3[39:32]@aftersbox_value_index1_%d_3[63:40]) ) ;\n" %(r,r,r,r,r,r) )
        fp.write("\n")
        for r in range(0,round):
            fp.write("ASSERT( middlelinearlayer_value_index1_%d_4 = BVXOR(aftersbox_value_index1_%d_4,aftersbox_value_index1_%d_4[3:0]@aftersbox_value_index1_%d_4[31:4]@aftersbox_value_index1_%d_4[34:32]@aftersbox_value_index1_%d_4[63:35]) ) ;\n" %(r,r,r,r,r,r) )
            fp.write("ASSERT( afterlinearlayer_value_index1_%d_4 = BVXOR(middlelinearlayer_value_index1_%d_4,aftersbox_value_index1_%d_4[51:32]@aftersbox_value_index1_%d_4[63:52]@aftersbox_value_index1_%d_4[19:0]@aftersbox_value_index1_%d_4[31:20]) ) ;\n" %(r,r,r,r,r,r) )
        fp.write("\n")
        
        for r in range(0,round+1):
            for i in range(0,5):
                fp.write("afterxor_value_index2_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")
        
        for r in range(0,round):
            for i in range(0,5):
                fp.write("middlesbox_1_value_index2_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")
        for r in range(0,round):
            for i in range(0,5):
                fp.write("middlesbox_2_value_index2_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")
        for r in range(0,round):
            for i in range(0,5):
                fp.write("middlesbox_3_value_index2_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")   
        for r in range(0,round):
            for i in range(0,5):
                fp.write("middlesbox_4_value_index2_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")
        for r in range(0,round):
            for i in range(0,5):
                fp.write("aftersbox_value_index2_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")
        
        for r in range(0,round):
            for i in range(0,5):
                fp.write("middlelinearlayer_value_index2_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")
        for r in range(0,round):
            for i in range(0,5):
                fp.write("afterlinearlayer_value_index2_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")        

        
        for r in range(0,round+1):
            fp.write("ASSERT( (index2_%d[1:0] = 0bin00) => (afterxor_value_index2_%d_0[31:0] = BVXOR(c_value_index2_%d_0[31:0],x_value_0)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[1:0] = 0bin01) => (afterxor_value_index2_%d_0[31:0] = BVXOR(c_value_index2_%d_0[31:0],x_value_1)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[1:0] = 0bin10) => (afterxor_value_index2_%d_0[31:0] = BVXOR(c_value_index2_%d_0[31:0],x_value_2)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[1:0] = 0bin11) => (afterxor_value_index2_%d_0[31:0] = BVXOR(c_value_index2_%d_0[31:0],x_value_3)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[3:2] = 0bin00) => (afterxor_value_index2_%d_1[31:0] = BVXOR(c_value_index2_%d_1[31:0],x_value_0)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[3:2] = 0bin01) => (afterxor_value_index2_%d_1[31:0] = BVXOR(c_value_index2_%d_1[31:0],x_value_1)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[3:2] = 0bin10) => (afterxor_value_index2_%d_1[31:0] = BVXOR(c_value_index2_%d_1[31:0],x_value_2)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[3:2] = 0bin11) => (afterxor_value_index2_%d_1[31:0] = BVXOR(c_value_index2_%d_1[31:0],x_value_3)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[5:4] = 0bin00) => (afterxor_value_index2_%d_2[31:0] = BVXOR(c_value_index2_%d_2[31:0],x_value_0)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[5:4] = 0bin01) => (afterxor_value_index2_%d_2[31:0] = BVXOR(c_value_index2_%d_2[31:0],x_value_1)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[5:4] = 0bin10) => (afterxor_value_index2_%d_2[31:0] = BVXOR(c_value_index2_%d_2[31:0],x_value_2)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[5:4] = 0bin11) => (afterxor_value_index2_%d_2[31:0] = BVXOR(c_value_index2_%d_2[31:0],x_value_3)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[7:6] = 0bin00) => (afterxor_value_index2_%d_3[31:0] = BVXOR(c_value_index2_%d_3[31:0],x_value_0)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[7:6] = 0bin01) => (afterxor_value_index2_%d_3[31:0] = BVXOR(c_value_index2_%d_3[31:0],x_value_1)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[7:6] = 0bin10) => (afterxor_value_index2_%d_3[31:0] = BVXOR(c_value_index2_%d_3[31:0],x_value_2)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[7:6] = 0bin11) => (afterxor_value_index2_%d_3[31:0] = BVXOR(c_value_index2_%d_3[31:0],x_value_3)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[9:8] = 0bin00) => (afterxor_value_index2_%d_4[31:0] = BVXOR(c_value_index2_%d_4[31:0],x_value_0)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[9:8] = 0bin01) => (afterxor_value_index2_%d_4[31:0] = BVXOR(c_value_index2_%d_4[31:0],x_value_1)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[9:8] = 0bin10) => (afterxor_value_index2_%d_4[31:0] = BVXOR(c_value_index2_%d_4[31:0],x_value_2)) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( (index2_%d[9:8] = 0bin11) => (afterxor_value_index2_%d_4[31:0] = BVXOR(c_value_index2_%d_4[31:0],x_value_3)) ) ;\n" %(r,r,r) ) 
        fp.write("\n") 
        
        for r in range(0,round+1):
            for i in range(0,5):
                fp.write("ASSERT( afterxor_value_index2_%d_%d[63:32] = c_value_index2_%d_%d[63:32] ) ;\n" %(r,i,r,i) )
        fp.write("\n")
        
        for r in range(0,round):
            fp.write("ASSERT( middlesbox_1_value_index2_%d_0 = BVXOR(afterxor_value_index2_%d_0,afterxor_value_index2_%d_4) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_1_value_index2_%d_1 = afterxor_value_index2_%d_1 ) ;\n" %(r,r) )
            fp.write("ASSERT( middlesbox_1_value_index2_%d_2 = BVXOR(afterxor_value_index2_%d_2,afterxor_value_index2_%d_1) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_1_value_index2_%d_3 = afterxor_value_index2_%d_3 ) ;\n" %(r,r) )
            fp.write("ASSERT( middlesbox_1_value_index2_%d_4 = BVXOR(afterxor_value_index2_%d_4,afterxor_value_index2_%d_3) ) ;\n" %(r,r,r) )
        fp.write("\n")        
        for r in range(0,round):
            fp.write("ASSERT( middlesbox_2_value_index2_%d_0 = (~middlesbox_1_value_index2_%d_0) & middlesbox_1_value_index2_%d_1 ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_2_value_index2_%d_1 = (~middlesbox_1_value_index2_%d_1) & middlesbox_1_value_index2_%d_2 ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_2_value_index2_%d_2 = (~middlesbox_1_value_index2_%d_2) & middlesbox_1_value_index2_%d_3 ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_2_value_index2_%d_3 = (~middlesbox_1_value_index2_%d_3) & middlesbox_1_value_index2_%d_4 ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_2_value_index2_%d_4 = (~middlesbox_1_value_index2_%d_4) & middlesbox_1_value_index2_%d_0 ) ;\n" %(r,r,r) )
        fp.write("\n")       
        for r in range(0,round):
            fp.write("ASSERT( middlesbox_3_value_index2_%d_0 = BVXOR(middlesbox_1_value_index2_%d_0,middlesbox_2_value_index2_%d_1) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_3_value_index2_%d_1 = BVXOR(middlesbox_1_value_index2_%d_1,middlesbox_2_value_index2_%d_2) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_3_value_index2_%d_2 = BVXOR(middlesbox_1_value_index2_%d_2,middlesbox_2_value_index2_%d_3) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_3_value_index2_%d_3 = BVXOR(middlesbox_1_value_index2_%d_3,middlesbox_2_value_index2_%d_4) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_3_value_index2_%d_4 = BVXOR(middlesbox_1_value_index2_%d_4,middlesbox_2_value_index2_%d_0) ) ;\n" %(r,r,r) )
        fp.write("\n")       
        for r in range(0,round):
            fp.write("ASSERT( middlesbox_4_value_index2_%d_0 = BVXOR(middlesbox_3_value_index2_%d_0,middlesbox_3_value_index2_%d_4) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_4_value_index2_%d_1 = BVXOR(middlesbox_3_value_index2_%d_0,middlesbox_3_value_index2_%d_1) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_4_value_index2_%d_2 = middlesbox_3_value_index2_%d_2 ) ;\n" %(r,r) )
            fp.write("ASSERT( middlesbox_4_value_index2_%d_3 = BVXOR(middlesbox_3_value_index2_%d_2,middlesbox_3_value_index2_%d_3) ) ;\n" %(r,r,r) )
            fp.write("ASSERT( middlesbox_4_value_index2_%d_4 = middlesbox_3_value_index2_%d_4 ) ;\n" %(r,r) )
        fp.write("\n")       
        for r in range(0,round):
            fp.write("ASSERT( aftersbox_value_index2_%d_0 = middlesbox_4_value_index2_%d_0 ) ;\n" %(r,r) )
            fp.write("ASSERT( aftersbox_value_index2_%d_1 = middlesbox_4_value_index2_%d_1 ) ;\n" %(r,r) )
            fp.write("ASSERT( aftersbox_value_index2_%d_2 = ~middlesbox_4_value_index2_%d_2 ) ;\n" %(r,r) )
            fp.write("ASSERT( aftersbox_value_index2_%d_3 = middlesbox_4_value_index2_%d_3 ) ;\n" %(r,r) )
            fp.write("ASSERT( aftersbox_value_index2_%d_4 = middlesbox_4_value_index2_%d_4 ) ;\n" %(r,r) )
        fp.write("\n")
        
        for r in range(0,round):
            fp.write("ASSERT( middlelinearlayer_value_index2_%d_0 = BVXOR(aftersbox_value_index2_%d_0,aftersbox_value_index2_%d_0[9:0]@aftersbox_value_index2_%d_0[31:10]@aftersbox_value_index2_%d_0[40:32]@aftersbox_value_index2_%d_0[63:41]) ) ;\n" %(r,r,r,r,r,r) )
            fp.write("ASSERT( afterlinearlayer_value_index2_%d_0 = BVXOR(middlelinearlayer_value_index2_%d_0,aftersbox_value_index2_%d_0[45:32]@aftersbox_value_index2_%d_0[63:46]@aftersbox_value_index2_%d_0[13:0]@aftersbox_value_index2_%d_0[31:14]) ) ;\n" %(r,r,r,r,r,r) )
        fp.write("\n")       
        for r in range(0,round):
            fp.write("ASSERT( middlelinearlayer_value_index2_%d_1 = BVXOR(aftersbox_value_index2_%d_1,aftersbox_value_index2_%d_1[30:0]@aftersbox_value_index2_%d_1[31:31]@aftersbox_value_index2_%d_1[61:32]@aftersbox_value_index2_%d_1[63:62]) ) ;\n" %(r,r,r,r,r,r) )
            fp.write("ASSERT( afterlinearlayer_value_index2_%d_1 = BVXOR(middlelinearlayer_value_index2_%d_1,aftersbox_value_index2_%d_1[50:32]@aftersbox_value_index2_%d_1[63:51]@aftersbox_value_index2_%d_1[18:0]@aftersbox_value_index2_%d_1[31:19]) ) ;\n" %(r,r,r,r,r,r) )
        fp.write("\n")    
        for r in range(0,round):
            fp.write("ASSERT( middlelinearlayer_value_index2_%d_2 = BVXOR(aftersbox_value_index2_%d_2,aftersbox_value_index2_%d_2[0:0]@aftersbox_value_index2_%d_2[31:1]@aftersbox_value_index2_%d_2[63:32]) ) ;\n" %(r,r,r,r,r) )
            fp.write("ASSERT( afterlinearlayer_value_index2_%d_2 = BVXOR(middlelinearlayer_value_index2_%d_2,aftersbox_value_index2_%d_2[34:32]@aftersbox_value_index2_%d_2[63:35]@aftersbox_value_index2_%d_2[2:0]@aftersbox_value_index2_%d_2[31:3]) ) ;\n" %(r,r,r,r,r,r) )
        fp.write("\n")  
        for r in range(0,round):
            fp.write("ASSERT( middlelinearlayer_value_index2_%d_3 = BVXOR(aftersbox_value_index2_%d_3,aftersbox_value_index2_%d_3[36:32]@aftersbox_value_index2_%d_3[63:37]@aftersbox_value_index2_%d_3[4:0]@aftersbox_value_index2_%d_3[31:5]) ) ;\n" %(r,r,r,r,r,r) )
            fp.write("ASSERT( afterlinearlayer_value_index2_%d_3 = BVXOR(middlelinearlayer_value_index2_%d_3,aftersbox_value_index2_%d_3[8:0]@aftersbox_value_index2_%d_3[31:9]@aftersbox_value_index2_%d_3[39:32]@aftersbox_value_index2_%d_3[63:40]) ) ;\n" %(r,r,r,r,r,r) )
        fp.write("\n")    
        for r in range(0,round):
            fp.write("ASSERT( middlelinearlayer_value_index2_%d_4 = BVXOR(aftersbox_value_index2_%d_4,aftersbox_value_index2_%d_4[3:0]@aftersbox_value_index2_%d_4[31:4]@aftersbox_value_index2_%d_4[34:32]@aftersbox_value_index2_%d_4[63:35]) ) ;\n" %(r,r,r,r,r,r) )
            fp.write("ASSERT( afterlinearlayer_value_index2_%d_4 = BVXOR(middlelinearlayer_value_index2_%d_4,aftersbox_value_index2_%d_4[51:32]@aftersbox_value_index2_%d_4[63:52]@aftersbox_value_index2_%d_4[19:0]@aftersbox_value_index2_%d_4[31:20]) ) ;\n" %(r,r,r,r,r,r) )
        fp.write("\n")
        
      
        for r in range(0,round):
            for i in range(0,5):
                fp.write("ASSERT( c_value_index1_%d_%d = afterlinearlayer_value_index1_%d_%d ) ;\n" %(r+1,i,r,i) )
        fp.write("\n")
        
        for r in range(0,round):
            for i in range(0,5):
                fp.write("ASSERT( c_value_index2_%d_%d = afterlinearlayer_value_index2_%d_%d ) ;\n" %(r+1,i,r,i) )
        fp.write("\n")      
        
        for r in range(0,round+1):
            for i in range(0,5):
                fp.write("c_difference_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")
        
        for r in range(0,round+1):
            for i in range(0,5):
                fp.write("ASSERT( c_difference_%d_%d = BVXOR(c_value_index1_%d_%d,c_value_index2_%d_%d) ) ;\n" %(r,i,r,i,r,i) )
        fp.write("\n")
     
        for r in range(0,round+1):
            for i in range(0,5):
                fp.write("afterxor_difference_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")
        
        for r in range(0,round+1):
            for i in range(0,5):
                fp.write("ASSERT( afterxor_difference_%d_%d = BVXOR(afterxor_value_index1_%d_%d,afterxor_value_index2_%d_%d) ) ;\n" %(r,i,r,i,r,i) )
        fp.write("\n")
        
        for r in range(0,round):
            for i in range(0,5):
                fp.write("aftersbox_difference_%d_%d: BITVECTOR(64) ;\n" %(r,i) )
        fp.write("\n")

        for r in range(0,round):
            for i in range(0,5):
                fp.write("ASSERT( aftersbox_difference_%d_%d = BVXOR(aftersbox_value_index1_%d_%d,aftersbox_value_index2_%d_%d) ) ;\n" %(r,i,r,i,r,i) )
        fp.write("\n")

        
        fp.write("ASSERT( afterxor_difference_2_0 = 0hex0000000000000000 ) ;\n")
        fp.write("ASSERT( afterxor_difference_2_1 = 0hex0000000040000008 ) ;\n")
        fp.write("ASSERT( afterxor_difference_2_2 = 0hex0000000040000008 ) ;\n")
        fp.write("ASSERT( afterxor_difference_2_3 = 0hex0000000040000008 ) ;\n")
        fp.write("ASSERT( afterxor_difference_2_4 = 0hex0000000000000000 ) ;\n")
        fp.write("\n")                                              
        fp.write("ASSERT( aftersbox_difference_2_0 = 0hex0000000000000000 ) ;\n")
        fp.write("ASSERT( aftersbox_difference_2_1 = 0hex0000000000000000 ) ;\n")
        fp.write("ASSERT( aftersbox_difference_2_2 = 0hex0000000000000000 ) ;\n")
        fp.write("ASSERT( aftersbox_difference_2_3 = 0hex0000000000000008 ) ;\n")
        fp.write("ASSERT( aftersbox_difference_2_4 = 0hex0000000040000000 ) ;\n")
        fp.write("\n")
        fp.write("ASSERT( afterxor_difference_3_0 = 0hex0000000000000000 ) ;\n")
        fp.write("ASSERT( afterxor_difference_3_1 = 0hex0000000040000400 ) ;\n")
        fp.write("ASSERT( afterxor_difference_3_2 = 0hex0000000040000400 ) ;\n")
        fp.write("ASSERT( afterxor_difference_3_3 = 0hex0400000000000000 ) ;\n")
        fp.write("ASSERT( afterxor_difference_3_4 = 0hex0400000000000000 ) ;\n")
        fp.write("\n")
        fp.write("ASSERT( aftersbox_difference_3_0 = 0hex0000000000000000 ) ;\n")
        fp.write("ASSERT( aftersbox_difference_3_1 = 0hex0000000000000000 ) ;\n")
        fp.write("ASSERT( aftersbox_difference_3_2 = 0hex0000000000000000 ) ;\n")
        fp.write("ASSERT( aftersbox_difference_3_3 = 0hex0000000000000000 ) ;\n")
        fp.write("ASSERT( aftersbox_difference_3_4 = 0hex0400000040000400 ) ;\n")
        fp.write("\n") 
        fp.write("ASSERT( afterxor_difference_4_0 = 0hex0000000000000000 ) ;\n")
        fp.write("ASSERT( afterxor_difference_4_1 = 0hex0000000000000000 ) ;\n")
        fp.write("ASSERT( afterxor_difference_4_2 = 0hex0000000000000000 ) ;\n")
        fp.write("ASSERT( afterxor_difference_4_3 = 0hex0000000000000000 ) ;\n")
        fp.write("ASSERT( afterxor_difference_4_4 = 0hex0000000000000000 ) ;\n")
        fp.write("\n")
        
        fp.close()

def generatepair():

    index_list = []
    index_str = []

    for i in range(20):
        index_list.append( random.randint(0,1) )
    
    for i in range(20):
        index_str.append( str(index_list[i]) )
    
    index = ''.join(index_str)
    
    return index

def pickinitialstate(keyindex):
    # the folder "p13-1-result" contains values of initial states ( including c and x ) that satisfy our differential characteristics ( with the probability 2^{-13} )
    hp = open('./p13-1-result/p13-1-'+str(keyindex)+'.txt','r')
    lines = hp.read()
    
    x = []
    
    for i in ['x_']:
        for k in range(0,4):
            text = re.compile('(?<='+" "+str(i)+str(k)+' \= 0x)[A-Fa-f0-9]{1,20}(?= \);)')
            tex = text.findall(lines)
            x.append(tex[0])
    
    c = []

    for i in ['c_']:
        for k in range(0,5):
            text = re.compile('(?<='+" "+str(i)+str(k)+' \= 0x)[A-Fa-f0-9]{1,20}(?= \);)')
            tex = text.findall(lines)
            c.append(tex[0])
    
    hp.close()
    
    return c,x

def writeinitialstate(keyindex,trailindex,xstate,cstate):
    
    fp = open( './'+str(keyindex)+'/'+str(trailindex)+'.cvc', 'a' )
    
    fp.write("ASSERT( x_value_0 = 0hex%s ) ;\n" %(xstate[0]))
    fp.write("ASSERT( x_value_1 = 0hex%s ) ;\n" %(xstate[1]))
    fp.write("ASSERT( x_value_2 = 0hex%s ) ;\n" %(xstate[2]))
    fp.write("ASSERT( x_value_3 = 0hex%s ) ;\n" %(xstate[3]))
    fp.write("\n")

    fp.write("ASSERT( c_value_index1_0_0 = 0hex%s );\n" %(cstate[0]))
    fp.write("ASSERT( c_value_index1_0_1 = 0hex%s );\n" %(cstate[1]))
    fp.write("ASSERT( c_value_index1_0_2 = 0hex%s );\n" %(cstate[2]))
    fp.write("ASSERT( c_value_index1_0_3 = 0hex%s );\n" %(cstate[3]))
    fp.write("ASSERT( c_value_index1_0_4 = 0hex%s );\n" %(cstate[4]))
    fp.write("\n")          
    fp.write("ASSERT( c_value_index2_0_0 = 0hex%s );\n" %(cstate[0]))
    fp.write("ASSERT( c_value_index2_0_1 = 0hex%s );\n" %(cstate[1]))
    fp.write("ASSERT( c_value_index2_0_2 = 0hex%s );\n" %(cstate[2]))
    fp.write("ASSERT( c_value_index2_0_3 = 0hex%s );\n" %(cstate[3]))
    fp.write("ASSERT( c_value_index2_0_4 = 0hex%s );\n" %(cstate[4]))
    fp.write("\n")
    
    fp.close()

def writecvc(keyindex,trailindex,index):
    fp = open( './'+str(keyindex)+'/'+str(trailindex)+'.cvc', 'a' )
    fp.write("ASSERT( index = 0bin"+str(index)+" ) ;\n")
    fp.write("QUERY(FALSE) ;\n")
    fp.write("COUNTEREXAMPLE ;\n")
    fp.close()

def check(keyindex,trailnumber):

    p = open( './'+str(keyindex)+'/result.txt', 'a' )
    
    pairset =  []
    i = 0
    trailindex = 0
    
    while trailindex<trailnumber:
        index = generatepair()
        
        if index not in pairset:
            p.write("i = "+str(i)+" trailindex = "+str(trailindex)+": "+str(index)+"\n")
            
            pairset.append(index)
            
            state = pickinitialstate(keyindex)
            cstate = state[0]
            xstate = state[1]
            
            cvc(keyindex,trailindex)
            writeinitialstate(keyindex,trailindex,xstate,cstate)
            writecvc(keyindex,trailindex,index)
            
            try:
                res = subprocess.check_output(["bash", "order.sh", "./"+str(keyindex)+"/"+str(trailindex)+".cvc",  "./"+str(keyindex)+"/"+str(trailindex)+".txt"])
                print "res:\n" + str(res)
            except Exception as E:
                print E
            
            rp = open('res.txt','a')
            rp.write(res)
            
            sleep(1)
            
            while True :
                thr = os.path.getsize('./'+str(keyindex)+'/'+str(trailindex)+".txt")
                if thr==0 :
                    sleep(1)
                else:
                    sleep(1)
                    os.remove('./'+str(keyindex)+'/'+str(trailindex)+".cvc")
                    trailindex = trailindex + 1
                    
                    break
            if thr<8 :
                os.remove('./'+str(keyindex)+'/'+str(trailindex-1)+".txt")
            else:
                p.write("collision\n")
        else:
            i = i + 1
    p.close()
    print i

trailnumber = 8192
for keyindex in range(0,600):
    os.mkdir(str(keyindex))
    check(keyindex,trailnumber)
