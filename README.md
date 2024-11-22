
# Test Directory Tree Generator

Ce script Python génère une arborescence de fichiers et de dossiers pour des tests, avec des paramètres personnalisables pour contrôler la profondeur, le nombre de fichiers, le nombre de sous-dossiers, et plus encore.

## Description

Le script crée une structure de répertoires avec des fichiers au sein de ces répertoires, selon des spécifications définies par l'utilisateur. Il est possible de définir des templates pour les noms de fichiers, les noms de dossiers et le contenu des fichiers. Le script prend également en charge des contraintes sur le nombre total de fichiers et de dossiers créés.

### Fonctionnalités

- Crée une arborescence de répertoires avec des fichiers à différents niveaux de profondeur.
- Paramètres personnalisables pour le nombre de fichiers, de sous-dossiers, et la profondeur.
- Possibilité de définir des contraintes sur le nombre total de fichiers et de dossiers.
- Affiche l'arborescence générée sous forme de texte à la manière de la commande `tree`.

## Prérequis

Le script nécessite Python 3.6 ou une version plus récente.

## Installation

Clonez le repository et installez les dépendances nécessaires (si nécessaire) :

```bash
git clone https://github.com/votre-utilisateur/test-directory-tree-generator.git
cd test-directory-tree-generator
```

Aucune dépendance externe n'est nécessaire.

## Utilisation

### Syntaxe de la commande

```bash
python generate_tree.py <chemin_du_dossier_racine> [options]
```

### Options

- `base_path`: Le chemin du dossier racine où l'arborescence sera créée. (Obligatoire)
- `--min_depth`: Profondeur minimale de l'arborescence (par défaut `1`).
- `--max_depth`: Profondeur maximale de l'arborescence (par défaut `5`).
- `--min_files`: Nombre minimum de fichiers par dossier (par défaut `1`).
- `--max_files`: Nombre maximum de fichiers par dossier (par défaut `5`).
- `--min_dirs`: Nombre minimum de sous-dossiers par dossier (par défaut `1`).
- `--max_dirs`: Nombre maximum de sous-dossiers par dossier (par défaut `3`).
- `--file_name`: Template pour les noms de fichiers (par défaut `file_{index}.txt`).
- `--subdir_name`: Template pour les sous-dossiers (par défaut `subdir_{index}`).
- `--file_content`: Template pour le contenu des fichiers (par défaut `This is the content of {file_name}.`).
- `--min_files_total`: Nombre minimum total de fichiers.
- `--max_files_total`: Nombre maximum total de fichiers.
- `--exact_files_total`: Nombre exact total de fichiers.
- `--min_dirs_total`: Nombre minimum total de dossiers.
- `--max_dirs_total`: Nombre maximum total de dossiers.
- `--exact_dirs_total`: Nombre exact total de dossiers.
- `--tree`: Affiche l'arborescence complète après la création.

### Exemple d'utilisation

```bash
python generate_tree.py /path/to/directory --max_depth 3 --min_files 2 --max_files 5 --tree
```

Cela générera une arborescence avec une profondeur maximale de 3, entre 2 et 5 fichiers par dossier, et affichera l'arborescence à la fin.

### Résultat

Le script génère une structure de répertoires et crée des fichiers à l'intérieur de ceux-ci. Une fois l'arborescence terminée, le script affiche un résumé avec le nombre total de fichiers et de dossiers créés, puis, si l'option `--tree` est activée, il affiche l'arborescence de manière similaire à la commande `tree`.

---

### Licence

Ce projet est sous licence [MIT](LICENSE).
