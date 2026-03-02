# EAIS Wiki Publisher
# This script clones the GitHub Wiki repo and syncs it with docs/wiki/

$repoUrl = "https://github.com/ruchirhuchgol-del/EAIS.wiki.git"
$wikiSource = "docs/wiki"
$tempPath = "tmp_wiki_repo"

Write-Host "--- EAIS Wiki Publisher ---" -ForegroundColor Cyan

# Remove temp folder if it exists
if (Test-Path $tempPath) {
    Remove-Item $tempPath -Recurse -Force
}

# Clone the wiki repository
Write-Host "Cloning GitHub Wiki repository..."
git clone $repoUrl $tempPath

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Could not clone Wiki repository. Ensure you have created the first page manually on GitHub." -ForegroundColor Red
    exit
}

# Copy files
Write-Host "Copying wiki files..."
Copy-Item "$wikiSource\*" $tempPath -Force

# Commit and Push
cd $tempPath
git add .
git commit -m "Update Wiki from docs/wiki"
Write-Host "Pushing to GitHub Wiki..."
git push origin master # Wikis often use 'master' as default

# Cleanup
cd ..
Remove-Item $tempPath -Recurse -Force

Write-Host "Wiki Update Complete!" -ForegroundColor Green
