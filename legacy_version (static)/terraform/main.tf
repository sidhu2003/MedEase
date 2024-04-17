resource "aws_key_pair" "medease_key" {
  key_name   = "medease"
  public_key = file("terraform_medease.pub")
}

resource "aws_instance" "terra_instance" {
  ami               = var.AMI[var.REGION]
  instance_type     = "t2.micro"
  availability_zone = var.ZONE
  key_name          = aws_key_pair.medease_key.key_name
  tags = {
    Name = "medease-instance"
  }

  vpc_security_group_ids = [aws_security_group.allow_http_traffic.id]

  provisioner "file" {
    source      = "setup.sh"
    destination = "/tmp/setup.sh"
  }

  provisioner "remote-exec" {
    inline = [
      "chmod u+x /tmp/setup.sh",
      "sudo /tmp/setup.sh"
    ]
  }

  connection {
    type        = "ssh"
    user        = var.user
    private_key = file("terraform_medease")
    host        = self.public_ip
  }
}
