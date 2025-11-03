variable "instance_name" {
  description = "Name of the VM instance"
  type        = string
}

variable "instance_machine_type" {
  description = "Machine type for the VM"
  type        = string
}

variable "zone" {
  description = "Zone where the VM will run"
  type        = string
}

variable "subnetwork_self_link" {
  description = "Self link of the subnetwork to attach the VM"
  type        = string
}

variable "instance_source_image" {
  description = "Source image for the VM boot disk"
  type        = string
}


