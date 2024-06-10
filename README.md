# RISC-V ALU Design Project

## Overview

In this project, I will design a RISC-V ALU. RISC-V is an instruction set architecture (ISA) that defines the functions a computer can carry out through assembly instructions. An ALU, or arithmetic and logic unit, performs many of the core computations dictated by those instructions. In short, I will be building a key component of a CPU.

The program I will use to create my ALU is Logisim, a free hardware-design and circuit-simulation tool. Logisim comes with libraries containing basic gates, memory chips, multiplexers and decoders, and other simple components.

## Circuits

### Circuit 1: LeftShift32

**LeftShift32:** `C = (B << Sa) | carrybits`

- **Inputs:** `B[32], Sa[5], Cin`

### Circuit 2: Add32

**Add32:** `C = A + B + Cin; V = overflow`

- **Inputs:** `A[32], B[32], Cin`
- **Outputs:** `C[32], V`

### Circuit 3: ALU32

**ALU32:** `(C, V) = fOp(A, B, Sa)`

- **Inputs:** `A[32], B[32], Op[4], Sa[5]`
- **Outputs:** `C[32], V`

| Op   | Name                   | C                                   | V           |
|------|------------------------|-------------------------------------|-------------|
| 0100 | and                    | C = A & B                           | V = 0       |
| 0105 | or                     | C = A \| B                          | V = 0       |
| 000x | shift left logical     | C = B << Sa                         | V = 0       |
| 1010 | xor                    | C = A ^ B                           | V = 0       |
| 1011 | nor                    | C = ~(A \| B)                       | V = 0       |
| 1100 | shift right logical    | C = B >>> Sa                        | V = 0       |
| 1101 | shift right arithmetic | C = B >> Sa                         | V = 0       |
| 1000 | ne                     | C = (A != B) ? 000...0001 : 000...0000 | V = 0   |
| 1001 | eq                     | C = (A == B) ? 000...0001 : 000...0000 | V = 0   |
| 1110 | le                     | C = (A ≤ 0) ? 000...0001 : 000...0000  | V = 0   |
| 1111 | gt                     | C = (A > 0) ? 000...0001 : 000...0000  | V = 0   |
| 011x | subtract               | C = A - B                           | V = overflow |
| 001x | add                    | C = A + B                           | V = overflow |
