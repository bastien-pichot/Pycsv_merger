# Guide d'utilisation - Outil de fusion CSV

## Présentation
Cet outil permet de fusionner plusieurs fichiers CSV en un seul fichier, en respectant une structure de colonnes définie par un fichier template.

## Prérequis importants
- Tous les fichiers doivent être au format CSV avec séparateur point-virgule (;)
- Les fichiers d'entrée doivent avoir exactement la même structure (mêmes colonnes) que le fichier template
- Les noms des fichiers n'ont pas d'importance

## Structure des dossiers
L'outil utilise trois dossiers qui sont créés automatiquement :
- `Inputs` : Dossier contenant les fichiers à fusionner
- `Template` : Dossier contenant le fichier modèle
- `Outputs` : Dossier où sera sauvegardé le résultat

## Étapes d'utilisation

### 1. Préparation du template
- Placez votre fichier template dans le dossier `Template`
- Ce fichier définit la structure des colonnes attendue
- **Important** : Vérifiez que votre template contient les bonnes colonnes dans le bon ordre

### 2. Préparation des fichiers à fusionner
- Placez tous les fichiers à fusionner dans le dossier `Inputs`
- **Important** : Vérifiez que tous vos fichiers :
  - Sont au format CSV avec séparateur point-virgule (;)
  - Ont exactement les mêmes colonnes que le template
  - Le nom des fichiers n'a pas d'importance

### 3. Fusion des fichiers
1. Double-cliquez sur l'exécutable `CSV_Merger.exe`
2. Cliquez sur le bouton "Start Merge"
3. Attendez que le processus se termine
4. Un message de confirmation apparaîtra une fois la fusion terminée

### 4. Récupération du résultat
- Le fichier fusionné sera disponible dans le dossier `Outputs`
- Le fichier de sortie sera au format CSV avec séparateur point-virgule (;)

## Résolution des problèmes courants

### Message d'erreur "No CSV files found in input folder"
➢ Vérifiez que :
- Vos fichiers sont bien dans le dossier `Inputs`
- Vos fichiers ont l'extension `.csv`

### Message d'erreur "No template CSV file found"
➢ Vérifiez que :
- Votre fichier template est bien dans le dossier `Template`
- Le fichier a l'extension `.csv`

### Message d'erreur "Column validation failed"
➢ Vérifiez que :
- Tous vos fichiers d'entrée ont exactement les mêmes colonnes que le template
- Les colonnes sont dans le même ordre
- Les noms des colonnes sont exactement identiques (attention aux espaces et à la casse)

## Notes importantes
- Les noms des fichiers n'ont aucune importance pour le fonctionnement de l'outil
- Seule la structure des colonnes doit être identique entre les fichiers
- L'outil traite les fichiers par lots pour gérer les grands volumes de données
- Il est recommandé de faire une sauvegarde de vos fichiers avant la fusion

## Support
En cas de problème :
1. Vérifiez que tous les prérequis sont respectés
2. Assurez-vous que tous les fichiers sont au bon format (CSV avec séparateur point-virgule)
3. Vérifiez la structure des colonnes de vos fichiers
