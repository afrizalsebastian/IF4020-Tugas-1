<?php

function navbar(){
    $navbar = <<< "EOT"
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Kriptografi</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
                <a class="nav-link" href="../standard_vigenere/encryption.php">Vigenere Standard</a>
                <a class="nav-link" href="../autokey_vigenere/encryption.php">Autokey Vigenere</a>
                <a class="nav-link" href="../extended_vigenere/encryption.php">Extended Vigenere</a>
                <a class="nav-link">Affine Cipher</a>
                <a class="nav-link">Playfair Cipher</a>
                <a class="nav-link">Hill Cipher</a>
            </div>
            </div>
        </div>
    </nav>
    EOT;

    echo "$navbar";
}
?>