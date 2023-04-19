def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    file.write("Company, Position, Location \n")

    for job in jobs:
        file.write(f"{job['company']}, {job['position']}, {job['location']}\n")

    file.close()