<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <title>Playfair Cipher</title>
</head>
<body>
<?php
    include "../navbar.php";
    navbar();
?>  
    <h1 class="text-center" style="margin-top:15px;">Playfair Cipher Encryption</h1>
    <a href="decryption.php" class="btn btn-secondary" tabindex="-1" role="button" style="margin-top:15px;" >Make Decryption</a>
    <a href="encryption.php" class="btn btn-secondary" tabindex="-1" role="button" style="margin-top:15px;"  >Make Encryption</a>
        <div class="container text-center mt-5">
            <div class="row justify-content-around">
                <div class="col-5">
                    <h3>Plaintext</h3>
                    <div class="form-floating">
                        <textarea class="form-control" form="plaintextForm" name="plaintext" placeholder="Write down your Plaintext" id="plainTextArea" style="height: 600px; overflow-y: auto; resize:none;"></textarea>
                        <label for="plainTextArea">Plaintext</label>
                    </div>
                </div>
                <div class="col-2">
                    <form method="post" id="plaintextForm" class="mt-3">
                        <h3>Key</h3>
                        <?php 
                            for ($i = 0; $i<5; $i++) {
                                echo "<div class='input-group mb-3'>";
                                for($j = 0; $j < 5; $j++){
                                    echo "<input type='text' name='key-".$i .$j ."' " ."class='form-control' aria-label='Sizing example input' aria-describedby='inputGroup-sizing-default'>";
                                }
                                echo "</div>";
                            }
                        ?>
                        <button type="submit" class="btn btn-secondary" name="encrypt" value="submitPlaintext">Encrypt</button>
                    </form>
                </div>
                <div class="col-5">
                    <h3>Ciphertext</h3>
                    <div class="form-floating">
                        <textarea readonly class="form-control" name="plaintext" placeholder="Write down your Plaintext" id="cipherTextArea" style="height: 600px; overflow-y: auto; resize:none;"><?php
                            if(isset($_POST['encrypt'])){
                                $plaintext = $_POST['plaintext'] ;
                                $key = "";
                                for ($i = 0; $i<5; $i++) {
                                    for($j = 0; $j < 5; $j++){
                                        $key .= $_POST['key-'.$i.$j];
                                    }
                                    
                                }
                                $download = "../../download/Cipher.txt";
                                $output = shell_exec('python ../../backend/playfair_cipher.py encrypt ' ."\"".$plaintext ."\"" .' ' ."\"".$key."\"" .' ' ."\"".$download."\"");
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