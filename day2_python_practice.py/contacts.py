
contacts = {
    "rashid": "03486823519",
    "Naveed": "03092559850",
    "kashif": "03472009420"
}

# Original Contacts
print("Original Contacts:", contacts)

# Add
contacts["Ali"] = "03222222222"
contacts["Ahmed"] = "03000000000"
print("After Adding:", contacts)

# Read
print("Rashid's Number:", contacts["rashid"])

# Delete
del contacts["Ahmed"]
print("After Deleting:", contacts)

# Final Result
print("\nFinal Contact Book:")
print(contacts)
