variable "REGION" {
  default = "us-east-1"
}

variable "ZONE" {
  default = "us-east-1a"
}

variable "AMI" {
  type = map(any)
  default = {
    us-east-1 = "ami-080e1f13689e07408"
    us-east-2 = "ami-0cd59ecaf368e5ccf"
  }
}

variable "user" {
  default = "ubuntu"
}