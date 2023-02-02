<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <title>Vigenere Standard</title>
</head>
<body>
<?php
    include "../navbar.php";
    navbar();
?>  
    <h1 class="text-center">Standard Vigenere Cipher Decryption</h1>
    <a href="decryption.php" class="btn btn-secondary" tabindex="-1" role="button" style="margin-top:15px;" >Make Decryption</a>
    <a href="encryption.php" class="btn btn-secondary" tabindex="-1" role="button" style="margin-top:15px;" >Make Encryption</a>
        <div class="container text-center mt-5">
            <div class="row justify-content-around">
                <div class="col">
                    <h3>CipherText</h3>
                    <div class="form-floating">
                        <textarea class="form-control" form="ciphertextForm" name="plaintext" placeholder="Write down your Cipher" id="cipherTextArea" style="height: 600px; overflow-y: auto; resize:none;"></textarea>
                        <label for="plainTextArea">CipherText</label>
                    </div>
                    <form method="post" id="ciphertextForm" class="mt-3">
                        <div class="input-group mb-3">
                            <span class="input-group-text" id="inputGroup-sizing-default">Key</span>
                            <input type="text" name="key" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
                        </div>
                        <button type="submit" class="btn btn-secondary" name="decrypt" value="submitCiphertext">Decryption</button>
                    </form>
                </div>
                <div class="col">
                    <h3>Plaintext</h3>
                    <div class="form-floating">
                        <textarea readonly class="form-control" name="plaintext" placeholder="Write down your Plaintext" id="cipherTextArea" style="height: 600px; overflow-y: auto; resize:none;"><?php
                            if(isset($_POST['decrypt'])){
                                $plaintext = $_POST['plaintext'] ;
                                $key = $_POST['key'];
                                $output = shell_exec('python ../../backend/vigenere_standard.py decrypt ' .$plaintext .' ' .$key);
                                echo $output;
                            }
                        ?></textarea>
                        <label for="cipherTextArea">Plaintext</label>
                    </div>
                </div>
            </div>
        </div>
</body>
</html>