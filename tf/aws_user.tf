data "aws_caller_identity" "current" {}

output "account_id" {
  value = "${data.aws_caller_identity.current.account_id}"
}

output "caller_arn" {
  value = "${data.aws_caller_identity.current.arn}"
}

output "caller_user" {
  value = "${data.aws_caller_identity.current.user_id}"
}

#----Create new IAM user----
resource "aws_iam_user" "user10"{
  name = "km10"
  
  #tags = "${var.default_tags}"
  #tags = {
  #  "Created by" = "tf test",
  #  "used for" = "test"
  #}
  tags = merge(
    var.default_tags,{
      "Extra tag" = "extra"
    }
  )
}

