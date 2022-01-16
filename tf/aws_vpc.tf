
#------VPC------------
##create VPC
#resource "aws_vpc" "km-tf-vpc-01" {
#  cidr_block = "10.0.0.0/16"
#  tags = {
#      Name = "km-vpc by tf"
#  }
#}

#Filter for existing VPC
data "aws_vpc" "km-tf-vpc-01" {
  filter {
    name   = "tag:Name"
    values = ["km-vpc"]
  }
}

#print out
output "vpc_id" {
  value = data.aws_vpc.km-tf-vpc-01.id
  #value = "${data.aws_vpc.km-tf-vpc-01.id}"
}



