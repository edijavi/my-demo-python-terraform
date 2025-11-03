output "network_self_link" {
  value       = google_compute_network.vpc.self_link
  description = "Self link of the created VPC"
}

output "subnetwork_self_link" {
  value       = google_compute_subnetwork.subnet.self_link
  description = "Self link of the created subnet"
}


