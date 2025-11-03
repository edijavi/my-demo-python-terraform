output "instance_self_link" {
  value       = google_compute_instance.vm.self_link
  description = "Self link of the VM instance"
}

output "instance_nat_ip" {
  value       = google_compute_instance.vm.network_interface[0].access_config[0].nat_ip
  description = "External NAT IP of the VM instance"
}


