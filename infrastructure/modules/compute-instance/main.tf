resource "google_compute_instance" "vm" {
  name         = var.instance_name
  machine_type = var.instance_machine_type
  zone         = var.zone

  tags = ["web"]

  boot_disk {
    initialize_params {
      image = var.instance_source_image
    }
  }

  network_interface {
    subnetwork = var.subnetwork_self_link
    access_config {}
  }

  metadata_startup_script = <<-EOT
    #!/usr/bin/env bash
    set -euo pipefail
    apt-get update -y
    apt-get install -y nginx
    systemctl enable nginx
    systemctl start nginx
    echo "Hello from $(hostname)" > /var/www/html/index.nginx-debian.html
  EOT
}


