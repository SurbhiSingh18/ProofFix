# ProofFix

ProofFix is a Reliability-Aware Automated Program Repair system.

The system combines:
- Flaky test detection
- Spectrum-based fault localization
- LLM-based patch generation
- Automated patch verification

Overall workflow:

Test Failure
→ Flakiness Gating
→ Fault Localization
→ Context Extraction
→ LLM Patch Generation
→ Patch Application
→ Patch Verification
→ Verified Fix