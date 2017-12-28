#ifndef HIGGSCSANDWIDTH_H
#define HIGGSCSANDWIDTH_H

#define PI 3.14159

#define  ID_ggToH  1
#define  ID_VBF    2
#define  ID_WH     3
#define  ID_ZH     4
#define  ID_ttH    5
#define  ID_Total  0 

#include <iostream>
#include <cstdlib>
#include <cmath>
#include <fstream>
#include <string>

#include "TROOT.h"
#include "TF1.h"
#include "TGraph.h"
#include "TCanvas.h"


class HiggsCSandWidth_MELA
{

 public:

  HiggsCSandWidth_MELA(std::string fileLoc);
  ~HiggsCSandWidth_MELA();

  double HiggsWidth(int ID,double mH);

 private:

  std::string fileName;
  
  double mass_BR[217];
  double BR[26][217];

  int N_BR;
};

#endif
