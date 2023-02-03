<?php
    $file="";
    if(isset($_POST['btnFile'])){
        $myfile = fopen($_FILES['inputFile']['tmp_name'], "r") or die("Unable to open file!");
        $file = fread($myfile,filesize($_FILES['inputFile']['tmp_name']));
        fclose($myfile);
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <title>Affine Cipher</title>
</head>
<body>
<?php
    include "../navbar.php";
    navbar();
?>  
    <h1 class="text-center" style="margin-top:15px;">Affine Cipher Encryption</h1>
    <a href="decryption.php" class="btn btn-secondary" tabindex="-1" role="button" style="margin-top:15px;" >Make Decryption</a>
    <a href="encryption.php" class="btn btn-secondary" tabindex="-1" role="button" style="margin-top:15px;"  >Make Encryption</a>
        <div class="container text-center mt-5">
            <div class="row justify-content-around">
                <div class="col-5">
                    <h3>Plaintext</h3>
                    <div class="form-floating">
                        <textarea class="form-control" form="plaintextForm" name="plaintext" placeholder="Write down your Plaintext" id="plainTextArea" style="height: 600px; overflow-y: auto; resize:none;"><?= $file ?></textarea>
                        <label for="plainTextArea">Plaintext</label>
                    </div>
                    <form method="post" id="fileInput" enctype="multipart/form-data">
                        <div class="mb-3">
                            <label for="formFile" class="form-label">Input Your File Here</label>
                            <div class="row justify-content-around">
                                <input class="form-control col" type="file" id="formFile" name="inputFile" accept=".txt">
                                <button type="submit" class="btn btn-success col" name="btnFile" value="File">OK</button>
                            </div>
                        </div>
                    </form>
                </div>
                <div class="col-2">
                    <form method="post" id="plaintextForm" class="mt-3">
                    <h3>Key</h3>
                        <div class="input-group mb-3">
                            <input placeholder="KEY M"  type="text" name="key_m" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
                            <input placeholder="KEY B" type="text" name="key_b" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
                        </div>
                        <button type="submit" class="btn btn-secondary" name="encrypt" value="submitPlaintext">Encrypt</button>
                    </form>
                </div>
                <div class="col-5">
                    <h3>Ciphertext</h3>
                    <div class="form-floating">
                        <textarea readonly class="form-control" name="plaintext" placeholder="Write down your Plaintext" id="cipherTextArea" style="height: 600px; overflow-y: auto; resize:none;"><?php
                            if(isset($_POST['encrypt'])){
                                $plaintext = $_POST['plaintext'] ;
                                $key_m = $_POST['key_m'];
                                $key_b = $_POST['key_b'];
                                $download = "../../download/Cipher.txt";
                                $file = "";
                                $output = shell_exec('python ../../backend/affine_cipher.py encrypt ' ."\"".$plaintext ."\"" .' ' ."\"".$key_m."\"".' ' ."\"".$key_b."\"" .' ' ."\"".$download."\"");
                                echo $output;
                            }
                        ?></textarea>
                        <label for="cipherTextArea">CipherText</label>
                        <a href="../../download/Cipher.txt" download class="btn btn-primary" tabindex="-1" style="margin-top:15px;">Download</a>
                    </div>
                </div>
            </div>
        </div>
</body>
</html>