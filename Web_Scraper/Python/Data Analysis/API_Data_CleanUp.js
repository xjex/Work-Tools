const fs = require("fs");

// Read the JSON file
const jsonFilePath = "../Output/API.json"; // Replace with the actual path to your JSON file
const jsonData = fs.readFileSync(jsonFilePath, "utf-8");
const data = JSON.parse(jsonData);

// Function to extract the desired information
function extractData(problem) {
  return {
    id: problem.id,
    name: problem.name,
    status: problem.status,
    author: {
      id: problem.author.id,
      email: problem.author.email,
      firstName: problem.author.firstName,
      lastName: problem.author.lastName,
    },
    comments: problem.comments,
    Language: problem.tests.flatMap((test) => test.language.name),
    score: problem.score,
    authorId: problem.authorId,
    insertedAt: problem.insertedAt,
    updatedAt: problem.updatedAt,
    skillTags: problem.skillTags,
  };
}

// Extract data for each problem in the 'data' array
const extractedData = data.data.map(extractData);

// Write the extracted data to a new JSON file
const outputFilePath = "../Output/Clean_API.json"; // Replace with the desired output path
fs.writeFileSync(outputFilePath, JSON.stringify(extractedData, null, 2));

console.log(`Extracted data written to ${outputFilePath}`);
