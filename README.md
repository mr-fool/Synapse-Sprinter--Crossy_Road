# Real-Time Adaptive EMG Gaming Framework
*Repository: Synapse-Sprinter-Crossy Road*

## Overview
This repository demonstrates the practical implementation of the EMG gaming system described in our IEEE Open Journal of Signal Processing paper.

## Repository Scope & Limitations
### What This Code Includes
- Real-time EMG signal acquisition from Arduino
- Basic signal processing pipeline (filtering, RMS windowing)  
- Game control interface
- Proof-of-concept demonstration

### What This Code Does NOT Include
- Theoretical ROC analysis implementations
- PI convergence proofs
- Monte Carlo simulation scripts
- Ninapro DB1 validation routines

**Note**: Mathematical analyses (ROC bounds, detection theory, PI convergence proofs) are provided analytically in the research paper and do not require computational verification.

## Hardware Requirements
- Arduino Uno microcontroller ($25)
- BioAmp EXG Pill EMG acquisition module ($15-30)
- Disposable Ag/AgCl electrodes ($10)
- Total cost: <$100 USD

## Hardware Assembly
![Hardware Assembly](https://github.com/mr-fool/Synapse-Sprinter--Crossy_Road/assets/6241984/a8f4ad25-c266-44f9-9a65-9269394ef7e2)

### Wiring Configuration

| **Arduino Uno** | **BioAmp EXG Pill** |
|-----------------|----------------------|
| `A0`            | EMG-1 (Channel 1)    |
| `A1`            | EMG-2 (Channel 2)    |
| `5 V`           | `VCC`                |
| `GND`           | `GND`                |

> Connect the 3.5mm jack to Ag/AgCl electrodes, attach two leads per muscle group, and the system is operational in <2 minutes.

## Software Dependencies
- Python 3.x
- All required packages are listed in `requirements.txt`

### Installation
```bash
pip install -r requirements.txt
```

### Key Dependencies
- **pyserial**: Arduino communication interface
- **pygame**: Game engine and user interface
- **numpy**: Signal processing and mathematical operations

## Usage
1. Ensure Python is installed on your system
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Connect the Arduino hardware as specified in the wiring table
4. Run the main script:
   ```bash
   python main.py
   ```
5. Set `ARDUINO_MODE = True` in the code for hardware integration

## System Demonstration
The implementation provides a gaming interface that responds to real-time EMG signals, demonstrating the feasibility of low-cost muscle-controlled human-computer interfaces.

### Gameplay Interface
![Interface](https://github.com/mr-fool/Synapse-Sprinter--Crossy_Road/assets/6241984/e8571f4b-192e-4c43-9332-64eb24a2a535)

![Gameplay](https://github.com/mr-fool/Synapse-Sprinter--Crossy_Road/assets/6241984/a78e4d74-d79f-4ee7-b838-631ddd42b82c)

## Video Demonstration
Watch the system in operation: [YouTube Demo](https://www.youtube.com/watch?v=h2tqiaCLs98)

## Technical Implementation
This code demonstrates:
- Real-time EMG signal acquisition and processing
- Adaptive threshold-based muscle activation detection
- Game control interface with sub-50ms response times
- Multi-threaded architecture for concurrent data processing

For detailed algorithmic descriptions, mathematical analysis, and comprehensive validation results, refer to the accompanying research publication.

## Research Context
This implementation serves as a proof-of-concept for accessible EMG-based gaming systems designed to support neuromuscular rehabilitation. The work addresses critical barriers in assistive technology by reducing system costs by >90% compared to clinical-grade alternatives while maintaining real-time performance requirements.

## License
MIT License - Open source implementation supporting reproducible research.
