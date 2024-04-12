<h1 align="center">PUNCH2</h1>
<p align="center"><i>A residue-level Intrinsically Disordered Region/Protein(IDP/IDR) predictor trained on PDB and <a href="https://www.rcsb.org/">Disprot</a> Databases.</i></p>

## 📝 Description
PUNCH2 project belongs to a serious of PUNCH projects which focus on the Structure and Function prediction of Intrisically Diordered Protein/Region (IDP/IDR).
Currently we have <a href="https://github.com/deemeng/punch2">PUNCH2</a> for IDR structure prediction, and <a href="https://github.com/deemeng/punch_linker">PUNCH_Linker</a> and  <a href="https://github.com/deemeng/punch_linker_light">PUNCH_Linker_Light</a> for DFL prediction. 

## 🐣 Getting Started
Currently, we provide two ways to use this perdictor: Docker or Download source code from this Github.
### Pre-requirements
This predictor requires sequences embedded with ONEHOT, [ProtTrans](https://github.com/agemagician/ProtTrans), and [MSA Transformer](https://github.com/facebookresearch/esm).

Note, 
* File format should be `[SEQUENCE_NAME/ID].npy`, replace *SEQUENCE_NAME/ID* with the actural sequence ID, it should be the same as the name from `.fasta` file.
* Matrix shape: \
  **Onehot**: (1, 227, 21) \
  **ProtTrans**: (1, 227, 1024) \
  **MSA Transformer**: (1, 227, 768)

📣‼️If you don't have them available, please visit the **[embedding](https://github.com/deemeng/embedding)** section of our project first to embed the sequences.‼️

(We maintain this separation due to the requirements from [CAID3](https://caid.idpcentral.org/challenge), but we may edit or merge them in the future.)
### Docker
#### Dependencies
* Onehot, [ProtTrans](https://github.com/agemagician/ProtTrans), and [MSA Transformer](https://github.com/facebookresearch/esm) embedded sequences;
* Docker Desktop 4.27.2 or higher;
#### Installing
* Pull the Docker image from  <a href="https://hub.docker.com/repository/docker/dimeng851/punch2/tags">DockerHub</a>
  ```sh
  docker pull dimeng851/punch2:v1
  ```

#### Executing program
* RUN the following command:
  >Replace \
  >`CONTAINER_NAME` - anyname you like; \
  >`PATH_TO_INPUT_FASTA` - path to input file, which is **ONE** FASTA file including all query sequences; \
  >`PATH_TO_ONEHOT` - a folder which includes all ONEHOT embedded sequences; \
  >`PATH_TO_MSATRANS` - a folder which includes all MSA Transformer embedded sequences; \
  >`PATH_TO_PROTTRANS` - a folder which includes all protTrans embedded sequences; \
  >`PATH_OUTPUT` - a folder which will be used to save all outputs, including: a. timings.csv; b. disorder folder, where will keep all the prediction resulds.
  ```sh
  docker run -d \
  -it \
  --name [CONTAINER_NAME] \
  --mount type=bind,source=[PATH_TO_INPUT_FASTA],target=/punch2/data/input.fasta \
  --mount type=bind,source=[PATH_TO_ONEHOT],target=/punch2/data/onehot \
  --mount type=bind,source=[PATH_TO_MSATRANS],target=/punch2/data/msaTrans \
  --mount type=bind,source=[PATH_TO_PROTTRANS],target=/punch2/data/protTrans \
  --mount type=bind,source=[PATH_OUTPUT],target=/punch2/output \
  dimeng851/punch2:v1
  ```
  > 
  >An example:
  ```sh
  docker run -d \
  -it \
  --name punch2_con \
  --mount type=bind,source=/home/dimeng/caid3/test_idr.fasta,target=/punch2/data/input.fasta \
  --mount type=bind,source=/home/dimeng/project/idr/data/caid/features/onehot,target=/punch2/data/onehot \
  --mount type=bind,source=/home/dimeng/project/idr/data/caid/features/msaTrans,target=/punch2/data/msaTrans \
  --mount type=bind,source=/home/dimeng/project/idr/data/caid/features/protTrans,target=/punch2/data/protTrans \
  --mount type=bind,source=/home/dimeng/caid3/punch_idr_output,target=/punch2/output \
  dimeng851/punch2:v1
  ```
* Find the results in **OUTPUT** folder.

## Contact & Help 📩

Email Di.
```
di.meng@ucdconnect.ie
```

## Authors
📬 Di Meng - di.meng@ucdconnect.ie \
📬 Gianluca Pollastri - gianluca.pollastri@ucd.ie

## Project
>https://github.com/deemeng/punch2
