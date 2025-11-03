terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.35"
    }
  }
  backend "local" {}
}

provider "google" {
  project = var.project_id
  region  = var.region
}

module "network" {
  source                = "../../modules/network"
  network_name          = var.network_name
  subnet_name           = var.subnet_name
  subnet_ip_cidr_range  = var.subnet_ip_cidr_range
  region                = var.region
}

module "compute" {
  source                = "../../modules/compute-instance"
  instance_name         = var.instance_name
  instance_machine_type = var.instance_machine_type
  instance_source_image = var.instance_source_image
  zone                  = var.zone
  subnetwork_self_link  = module.network.subnetwork_self_link
}


