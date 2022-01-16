
#----AMI------
data "aws_ami" "amz-linux-free-tier" {
  most_recent = true

  filter {
   name   = "owner-alias"
   values = ["amazon"]
  }

  filter {
    name   = "name"
    #values = ["amzn2-ami-hvm-*"]
    values = ["amzn2-ami-hvm-*-x86_64-ebs"]
  }

  #filter {
  #     name   = "architecture"
  #     values = ["x86_64"]
  #}

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  owners = ["amazon"]
}

output "amz_linux_instance_id" {
  value = data.aws_ami.amz-linux-free-tier.id
}

#----EC2-----------------
resource "aws_instance" "km-tf-ec2-01" {
    ami   = data.aws_ami.amz-linux-free-tier.id
    instance_type = "t2.micro"
    tags = {
        Name = "km-ec2 by tf"
    }
    user_data = <<-EOF
      sudo yum update -y
      sudo yum install apache2 -y
      sudo systemctl start apache2
      sudo cp /var/www/html/index.html /var/www/html/index_bkp.html
      sudo bash -c 'echo "Welcome to home page" > /var/www/html/index.html'
      EOF
}

#print out
output "amz_linux_instance_public_ip" {
  value = aws_instance.km-tf-ec2-01.public_ip
}
