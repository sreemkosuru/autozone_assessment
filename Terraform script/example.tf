variable "<Google_Project_ID>" {
  description = "TF script to create pub/sub topics"
}

variable "topic_count" {
  description = "total pub/sub topics"
  default     = 10000
}

provider "google" {
  credentials = file("path/to/service-account-key.json")
  project     = var.Google_Project_ID
  region      = "us-central1"
}

resource "google_pubsub_topic" "topic" {
  count = var.topic_count

  name    = "topic-${count.index}"
  project = var.Google_Project_ID
}

output "topic_names" {
  value = google_pubsub_topic.topic[*].name
}