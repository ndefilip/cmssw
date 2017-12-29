#ifndef CommonTools_ParticleFlow_PackedCandidateWithSrcPtrFactor_h
#define CommonTools_ParticleFlow_PackedCandidateWithSrcPtrFactor_h

/**
  \class    reco::PFCandidateWithSrcPtrFactory PFCandidateWithSrcPtrFactory.h  "CommonTools/ParticleFlow/interface/PFCandidateWithSrcPtrFactory.h"
  \brief    Creates a PFCandidate from an input FwdPtr, and sets the "source" Ptr to the FwdPtr.backPtr 


  \author   Salvatore Rappoccio
*/

//#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
//#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"

#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

namespace reco {
  class PackedCandidateWithSrcPtrFactory : public std::unary_function<pat::PackedCandidate, edm::FwdPtr<pat::PackedCandidate> > {
  public :
    pat::PackedCandidate operator()( edm::FwdPtr<pat::PackedCandidate> const & input ) const {
      pat::PackedCandidate output( *input );
      /* really, what's the point in this ? The one below should be enough
      //and the one loop here is a torture of converting Ptr<PFCandidate> to Ptr<Candidate> and back
      for ( unsigned int isource = 0; isource < input->numberOfSourceCandidatePtrs(); ++isource ) {
	edm::Ptr<reco::PFCandidate> ptr (input->sourceCandidatePtr(isource) );
	output.setSourceCandidatePtr( ptr );
      }
      */
      output.setSourceCandidatePtr( input.backPtr() );
      return output; 
    }
  };
}

#endif
