#ifndef HIGGSCSANDWIDTH_CC
#define HIGGSCSANDWIDTH_CC


#include <iostream>
#include <cmath>
#include <string>
#include <cstdlib>
#include <fstream>

#include "TROOT.h"
#include "TF1.h"
#include "TGraph.h"
#include "TCanvas.h"
#include "TSpline.h"


#include "ZZMatrixElement/MELA/interface/HiggsCSandWidth_MELA.h"

using namespace std;

HiggsCSandWidth_MELA::HiggsCSandWidth_MELA(std::string fileLoc = "../txtFiles")
{

  N_BR = 217;

  ifstream file;
  // ---------------- Read BR into memory ------------------ //         
  //fileName = fileLoc+"/HiggsBR_Official.txt";
  fileName = fileLoc+"/HiggsTotalWidth.txt";
  file.open(fileName.c_str());
  for(int k = 0; k < N_BR; k++){

    file >> mass_BR[k] >> BR[0][k]; 

  }
  file.close();

}


HiggsCSandWidth_MELA::~HiggsCSandWidth_MELA()
{
  //destructor

}


// HiggsWidth takes process ID and higgs mass mH
double HiggsCSandWidth_MELA::HiggsWidth(int ID, double mH){


  /***********************IDs************************/
  /*                       Total = 0                */
  /**************************************************/



  //  double PartialWidth = 0;
  double Width = 0;
  int i = 0;
  double step;

  // If ID is unavailable return -1                                           
  if(ID > 25 || ID < 0){return -1;}


  // If mH is out of range return -1                                            
  // else find what array number to read                                        
  if( mH < 90 || mH > 1000){return -1;}
  else{

    //Find index and closest higgs mass for which we have numbers
    if(mH <=110 ){step = 5; i = (int)((mH - 90)/step);}
    if(mH > 110 && mH <= 140 ){step = 0.5; i = (int)(4 + (mH-110)/step);}
    if(mH > 140 && mH <= 160 ){step = 1; i = (int)(64 + (mH-140)/step); }
    if(mH > 160 && mH <= 290 ){step = 2; i = (int)(84 + (mH-160)/step); }
    if(mH > 290 && mH <= 350 ){step = 5; i = (int)(149 + (mH-290)/step); }
    if(mH > 350 && mH <= 400 ){step = 10; i = (int)(161 + (mH-350)/step); }
    if(mH > 400 && mH <= 600 ){step = 20; i = (int)(166 + (mH-400)/step); }
    if(mH > 600){step = 10; i = (int)(176 + (mH-600)/step); }


    if( ID == 0 )
      {
	if(i < 1){i = 1;}
	if(i+2 >= N_BR){i = N_BR - 3;}
	const int indexW = 4;
	double xmhW[indexW], sigW[indexW];
	xmhW[0]=mass_BR[i-1];xmhW[1]=mass_BR[i];xmhW[2]=mass_BR[i+1];xmhW[3]=mass_BR[i+2];
	sigW[0]=BR[ID][i-1]; sigW[1]=BR[ID][i]; sigW[2]=BR[ID][i+1]; sigW[3]=BR[ID][i+2];
	
	TGraph *graphW = new TGraph(indexW, xmhW, sigW);
	TSpline3 *gsW = new TSpline3("gsW",graphW);
	gsW->Draw();
	Width = gsW->Eval(mH);
	delete gsW;
	delete graphW;
      }
    else{
			cout << "ERROR! Only available for total width extraction!"<<endl;
			return 0;
    }
    
  }
  
  return Width;
  
} 

#endif
