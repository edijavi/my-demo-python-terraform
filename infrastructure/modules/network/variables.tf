variable "network_name" {
  description = "Name of the VPC network"
  type        = string
}

variable "subnet_name" {
  description = "Name of the subnet"
  type        = string
}

variable "subnet_ip_cidr_range" {
  description = "CIDR range for the subnet"
  type        = string
}

variable "region" {
  description = "Region for the subnet"
  type        = string
}


