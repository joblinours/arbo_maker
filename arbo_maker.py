import os
import random
import argparse


def create_test_tree(
    base_path,
    current_depth,
    min_depth,
    max_depth,
    min_files,
    max_files,
    min_dirs,
    max_dirs,
    file_name_template,
    subdir_name_template,
    file_content_template,
    min_files_total,
    max_files_total,
    exact_files_total,
    min_dirs_total,
    max_dirs_total,
    exact_dirs_total,
    total_tracker,
):
    """
    Crée une arborescence de test de manière récursive avec des paramètres personnalisables.
    """
    # Si la condition de nombre exact de fichiers ou de dossiers est atteinte, on arrête la création.
    if (exact_files_total and total_tracker["files"] >= exact_files_total) or (
        exact_dirs_total and total_tracker["dirs"] >= exact_dirs_total
    ):
        return

    # Calculer le nombre de fichiers et de sous-dossiers à créer
    num_files = random.randint(min_files, max_files)
    num_dirs = random.randint(min_dirs, max_dirs)

    # Appliquer les limites totales de fichiers et de dossiers
    if max_files_total > 0:
        num_files = min(num_files, max_files_total - total_tracker["files"])
    if max_dirs_total > 0:
        num_dirs = min(num_dirs, max_dirs_total - total_tracker["dirs"])

    # Appliquer les conditions exactes
    if exact_files_total:
        num_files = min(num_files, exact_files_total - total_tracker["files"])
    if exact_dirs_total:
        num_dirs = min(num_dirs, exact_dirs_total - total_tracker["dirs"])

    # Si le nombre de fichiers et de dossiers à créer est 0, on ne crée rien
    if num_files == 0 and num_dirs == 0:
        return

    # Créer les fichiers dans le dossier courant
    files_in_current_dir = 0
    for i in range(num_files):
        if exact_files_total and total_tracker["files"] >= exact_files_total:
            break
        file_name = file_name_template.replace(
            "{index}", str(total_tracker["files"] + 1)
        )
        file_path = os.path.join(base_path, file_name)
        with open(file_path, "w") as f:
            f.write(file_content_template.replace("{file_name}", file_name))
        total_tracker["files"] += 1
        files_in_current_dir += 1

    # Si le dossier n'a pas encore de fichier, on en ajoute un pour respecter la contrainte
    if files_in_current_dir == 0:
        file_name = file_name_template.replace(
            "{index}", str(total_tracker["files"] + 1)
        )
        file_path = os.path.join(base_path, file_name)
        with open(file_path, "w") as f:
            f.write(file_content_template.replace("{file_name}", file_name))
        total_tracker["files"] += 1
        files_in_current_dir = 1

    # Créer les sous-dossiers
    for i in range(num_dirs):
        if exact_dirs_total and total_tracker["dirs"] >= exact_dirs_total:
            break
        subdir_name = subdir_name_template.replace(
            "{index}", str(total_tracker["dirs"] + 1)
        )
        subdir_path = os.path.join(base_path, subdir_name)
        os.makedirs(subdir_path, exist_ok=True)
        total_tracker["dirs"] += 1

        # Recurse dans chaque sous-dossier si ce n'est pas déjà fini
        if (
            current_depth < max_depth
            and total_tracker["files"] < exact_files_total
            and total_tracker["dirs"] < exact_dirs_total
        ):
            create_test_tree(
                subdir_path,
                current_depth + 1,
                min_depth,
                max_depth,
                min_files,
                max_files,
                min_dirs,
                max_dirs,
                file_name_template,
                subdir_name_template,
                file_content_template,
                min_files_total,
                max_files_total,
                exact_files_total,
                min_dirs_total,
                max_dirs_total,
                exact_dirs_total,
                total_tracker,
            )


def print_tree(base_path, prefix=""):
    """
    Affiche l'arborescence des fichiers et des dossiers dans un format similaire à la commande `tree`.
    """
    # Lister tous les fichiers et sous-dossiers dans le dossier courant
    items = sorted(os.listdir(base_path))
    for item in items:
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path):
            print(f"{prefix}├── {item}")
            print_tree(item_path, prefix + "│   ")
        else:
            print(f"{prefix}├── {item}")


def main():
    # Configurer argparse avec des noms d'arguments simplifiés
    parser = argparse.ArgumentParser(
        description="Crée une arborescence de test avec des paramètres personnalisés."
    )
    parser.add_argument(
        "base_path", type=str, help="Chemin du dossier racine où créer l'arborescence."
    )
    parser.add_argument(
        "--min_depth",
        type=int,
        default=1,
        help="Profondeur minimale de l'arborescence.",
    )
    parser.add_argument(
        "--max_depth",
        type=int,
        default=5,
        help="Profondeur maximale de l'arborescence.",
    )
    parser.add_argument(
        "--min_files",
        type=int,
        default=1,
        help="Nombre minimum de fichiers par dossier.",
    )
    parser.add_argument(
        "--max_files",
        type=int,
        default=5,
        help="Nombre maximum de fichiers par dossier.",
    )
    parser.add_argument(
        "--min_dirs",
        type=int,
        default=1,
        help="Nombre minimum de sous-dossiers par dossier.",
    )
    parser.add_argument(
        "--max_dirs",
        type=int,
        default=3,
        help="Nombre maximum de sous-dossiers par dossier.",
    )
    parser.add_argument(
        "--file_name",
        type=str,
        default="file_{index}.txt",
        help="Template pour les noms des fichiers.",
    )
    parser.add_argument(
        "--subdir_name",
        type=str,
        default="subdir_{index}",
        help="Template pour les sous-dossiers.",
    )
    parser.add_argument(
        "--file_content",
        type=str,
        default="This is the content of {file_name}.",
        help="Template pour le contenu des fichiers.",
    )
    parser.add_argument(
        "--min_files_total",
        type=int,
        default=0,
        help="Nombre minimum total de fichiers.",
    )
    parser.add_argument(
        "--max_files_total",
        type=int,
        default=0,
        help="Nombre maximum total de fichiers.",
    )
    parser.add_argument(
        "--exact_files_total",
        type=int,
        default=0,
        help="Nombre exact total de fichiers.",
    )
    parser.add_argument(
        "--min_dirs_total",
        type=int,
        default=0,
        help="Nombre minimum total de dossiers.",
    )
    parser.add_argument(
        "--max_dirs_total",
        type=int,
        default=0,
        help="Nombre maximum total de dossiers.",
    )
    parser.add_argument(
        "--exact_dirs_total",
        type=int,
        default=0,
        help="Nombre exact total de dossiers.",
    )
    parser.add_argument(
        "--tree",
        action="store_true",
        help="Affiche l'arborescence une fois créée, comme la commande `tree`.",
    )

    args = parser.parse_args()

    # Créer le dossier racine si nécessaire
    if not os.path.exists(args.base_path):
        os.makedirs(args.base_path)

    total_tracker = {"files": 0, "dirs": 1}  # La racine compte comme un dossier

    create_test_tree(
        base_path=args.base_path,
        current_depth=1,
        min_depth=args.min_depth,
        max_depth=args.max_depth,
        min_files=args.min_files,
        max_files=args.max_files,
        min_dirs=args.min_dirs,
        max_dirs=args.max_dirs,
        file_name_template=args.file_name,
        subdir_name_template=args.subdir_name,
        file_content_template=args.file_content,
        min_files_total=args.min_files_total,
        max_files_total=args.max_files_total,
        exact_files_total=args.exact_files_total,
        min_dirs_total=args.min_dirs_total,
        max_dirs_total=args.max_dirs_total,
        exact_dirs_total=args.exact_dirs_total,
        total_tracker=total_tracker,
    )

    print(f"Arborescence créée avec succès dans {args.base_path}.")
    print(
        f"Statistiques : {total_tracker['dirs']} dossiers, {total_tracker['files']} fichiers."
    )

    # Si l'option --tree est activée, afficher l'arborescence
    if args.tree:
        print("\nArborescence:")
        print_tree(args.base_path)


if __name__ == "__main__":
    main()
