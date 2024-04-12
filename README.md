<h1 align="center">PUNCH_Linker</h1>
<p align="center"><i>A Disordered Flexible Linker (DFL) ppredictor trained on DLD domain Linker dataset and <a href="https://disprot.org/">Disprot</a> Database.</i></p>

## 📝 Description
PUNCH_Linker project belongs to a serious of PUNCH projects which focus on the Structure and Function prediction of Intrisically Diordered Protein/Region (IDP/IDR).
Currently we have <a href="https://disprot.org/">PUNCH2</a> for IDR structure prediction and <a href="https://disprot.org/">PUNCH_Linker</a> for DFL prediction.
PUNCH_Linker is trained on more than 2000 DFL linker dataset from <a href="https://disprot.org/">DLD</a> dataset and <a href="https://disprot.org/">Disprot</a>, its performance is better than TOP predictors on the CAID2 Linker dataset.

## 🐣 Getting Started
Currently, we provide two ways to use this perdictor: Docker or Download source code from this Github.
### Pre-requirements
This predictor requires sequences embedded with [ProtTrans](https://github.com/agemagician/ProtTrans) and [MSA Transformer](https://github.com/facebookresearch/esm).
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
* [ProtTrans](https://github.com/agemagician/ProtTrans) and [MSA Transformer](https://github.com/facebookresearch/esm) embedded sequences;
* Docker Desktop 4.27.2 or higher;
#### Installing
* Go to Dockerhub
* Get the project
  ```sh
  
  ``` 
### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
