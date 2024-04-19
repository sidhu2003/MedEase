resource "aws_ecr_repository" "medease" {
  name                 = "medease"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}