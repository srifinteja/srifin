package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import javax.validation.constraints.NotNull;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.ZoneId;

import org.springframework.web.bind.annotation.RequestMapping;

import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.GetMapping;
import java.time.format.DateTimeParseException;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
@RestController
@CrossOrigin(origins = "http://localhost:4200")
@RequestMapping("/api/census")
public class CensusController {
    private final ExcelReader excelReader;
// Constructor injection for ExcelReader

    private final UserService userService;

    @Autowired
    public CensusController(ExcelReader excelReader, UserService userService) {
        this.excelReader = excelReader;
        this.userService = userService;
    }

    @GetMapping("/unique-device-ids")
    public List<Object[]> getUniqueDeviceIds() {
        return userService.getDeviceIdCounts();
    }

    @GetMapping("/totalDistance")
    public ResponseEntity<?> getTotalDistance(
            @RequestParam("deviceId") String deviceId,
            @RequestParam("startTime") String startTimeStr,
            @RequestParam("endTime") String endTimeStr) {
        try {
            DateTimeFormatter formatter = DateTimeFormatter.ISO_DATE_TIME;
            LocalDateTime startTime = LocalDateTime.parse(startTimeStr, formatter);
            LocalDateTime endTime = LocalDateTime.parse(endTimeStr, formatter);

            long startEpoch = startTime.atZone(ZoneId.systemDefault()).toInstant().toEpochMilli();
            long endEpoch = endTime.atZone(ZoneId.systemDefault()).toInstant().toEpochMilli();

            if (startEpoch >= endEpoch) {
                return ResponseEntity.badRequest().body("The start time must be before the end time.");
            }

            double totalDistance = userService.findTotalDistanceByDeviceIdAndEpochDataBetween(deviceId, startEpoch, endEpoch);
            return ResponseEntity.ok(Map.of("totalDistance", totalDistance));
        } catch (DateTimeParseException e) {
            return ResponseEntity.badRequest().body("Failed to parse date-time: " + e.getMessage());
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body("An error occurred while calculating total distance: " + e.getMessage());
        }
    }

    @GetMapping
    public ResponseEntity<?> getAllGeolocations(
            @RequestParam("startTime") String startTimeStr,
            @RequestParam("endTime") String endTimeStr,
            @RequestParam(value = "deviceId", required = false) String deviceId,
            Pageable pageable) {

        // Parse startTimeStr and endTimeStr into LocalDateTime
        DateTimeFormatter formatter = DateTimeFormatter.ISO_DATE_TIME;
        LocalDateTime startTime = LocalDateTime.parse(startTimeStr, formatter);
        LocalDateTime endTime = LocalDateTime.parse(endTimeStr, formatter);

        // Convert LocalDateTime to epoch milliseconds
        long startEpoch = startTime.atZone(ZoneId.systemDefault()).toInstant().toEpochMilli();
        long endEpoch = endTime.atZone(ZoneId.systemDefault()).toInstant().toEpochMilli();

        try {
            Page<User_s> users;
            if (deviceId != null && !deviceId.trim().isEmpty()) {
                // Update the method call to include date filtering
                users = userService.findByDeviceIdAndEpochDataBetween(deviceId, startEpoch, endEpoch, pageable);
                if (users.isEmpty()) {
                    // Handle case where no users are found for the given deviceId and date range
                    return ResponseEntity.notFound().build();
                }
            } else {
                // If deviceId is not provided, consider how you want to handle this case.
                return ResponseEntity.badRequest().body("Device ID is required");
            }
            return ResponseEntity.ok(users);
        } catch (Exception e) {
            // Handle exceptions
            return new ResponseEntity<>("An error occurred while fetching geolocation data", HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }


//    private static final String BASE_DIRECTORY_PATH_15km = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\Surroundings\\";
////"C:\Users\Teja\Desktop\demo\BR_Sourroundings\Darbhanga_15_km.xlsx"
//    @GetMapping("/{cityName}Under15")
//    public ResponseEntity<List<Under15>> getCityData(@PathVariable String cityName) {
//        // Construct the file path dynamically based on the city name
//        String excelFilePath = BASE_DIRECTORY_PATH_15km + cityName + "_15_km.xlsx";
//
//        // Use the ExcelReader to read data from the Excel file
//        List<Under15> dataList = excelReader.readUnder15Data(excelFilePath);
//
//        // Return the list of data objects
//        return ResponseEntity.ok(dataList);
//    }
//
////    C:\Users\Teja\Desktop\karthik\demo\BR_Source
//    private static final String BASE_DIRECTORY_PATH_source = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\Surroundings\\";
//    //"C:\Users\Teja\Desktop\demo\BR_Sourroundings\Darbhanga_15_km.xlsx"
//    @GetMapping("/{cityName}Source")
//    public ResponseEntity<List<latestSourcing>> getSourceData(@PathVariable String cityName) {
//        // Construct the file path dynamically based on the city name
//        String excelFilePath = BASE_DIRECTORY_PATH_source + cityName + "_Source_Map.xlsx";
//
//        // Use the ExcelReader to read data from the Excel file
//        List<latestSourcing> dataList = excelReader.readLatestSourcing(excelFilePath);
//
//        // Return the list of data objects
//        return ResponseEntity.ok(dataList);
//    }
//
//    @GetMapping("/Combined")
//    public ResponseEntity<List<Combined>> getCombined() {
//        // Specify the path to your Excel file
//        String excelFilePath = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\combined_file (2).xlsx";
//        // Use the ExcelReader to read data from the Excel file
//        List<Combined> dataList = excelReader.combinedData(excelFilePath);
//        // Return the list of CensusData objects
//        return ResponseEntity.ok(dataList);
//    }

    @GetMapping("/upMapdata")
    public ResponseEntity<List<Mapdata>> getupMapdata() {
        // Specify the path to your Excel file
        String excelFilePath = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\radar\\up_data.xlsx";
        // Use the ExcelReader to read data from the Excel file
        List<Mapdata> dataList = excelReader.readLocationData(excelFilePath);
        // Return the list of CensusData objects
        return ResponseEntity.ok(dataList);
    }

    @GetMapping("/biharMapdata")
    public ResponseEntity<List<Mapdata>> getbiharMapdata() {
        // Specify the path to your Excel file
        String excelFilePath = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\radar\\bihar_data.xlsx";
        // Use the ExcelReader to read data from the Excel file
        List<Mapdata> dataList = excelReader.readLocationData(excelFilePath);
        // Return the list of CensusData objects
        return ResponseEntity.ok(dataList);
    }

    @GetMapping("/kaMapdata")
    public ResponseEntity<List<Mapdata>> getkaMapdata() {
        // Specify the path to your Excel file
        String excelFilePath = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\radar\\ka_data.xlsx";
        // Use the ExcelReader to read data from the Excel file
        List<Mapdata> dataList = excelReader.readLocationData(excelFilePath);
        // Return the list of CensusData objects
        return ResponseEntity.ok(dataList);
    }


//    @RestController
//    @RequestMapping("/api/village-boundaries")


//        @GetMapping("/text-file")
//        public ResponseEntity<String> getTextFileContent() {
//            // Read the text file
//            Path filePath = Paths.get("C:\\Users\\Teja\\Downloads\\shivpur_districts.geojson");
//            String content;
//            try {
//                content = new String(Files.readAllBytes(filePath));
//                return ResponseEntity.ok(content);
//            } catch (IOException e) {
//                // Handle file read error
//                return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Error reading file");
//            }
//        }

    //    @GetMapping("/latestSourcing")
//    public ResponseEntity<List<latestSourcing>> getLatestSourcing() {
//        // Specify the path to your Excel file
//        String excelFilePath = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\Shivpur_Source_Map.xlsx";
//        // Use the ExcelReader to read data from the Excel file
//        List<latestSourcing> dataList = excelReader.readLatestSourcing(excelFilePath);
//        // Return the list of CensusData objects
//        return ResponseEntity.ok(dataList);
//    }
//    @GetMapping("/MixData")
//    public ResponseEntity<List<Mix>> getMixData() {
//        // Specify the path to your Excel file
//        String excelFilePath = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\Basavakalyan_mix.xlsx";
//        // Use the ExcelReader to read data from the Excel file
//        List<Mix> dataList = excelReader.readMapData(excelFilePath);
//        // Return the list of CensusData objects
//        return ResponseEntity.ok(dataList);
//    }
    @GetMapping("/mixData/{fileName}")
    public ResponseEntity<List<Mix>> getMixData(@PathVariable String fileName) {
        // Base path to the Excel files
        String basePath = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\mixedd\\";
        // Construct the full path by appending the fileName parameter and file extension
        String excelFilePath = basePath + fileName + "_Mixed_Map.xlsx";

        // Use the ExcelReader to read data from the Excel file
        List<Mix> dataList = excelReader.readMapData(excelFilePath);

        // Return the list of Mix objects
        return ResponseEntity.ok(dataList);
    }

    @GetMapping("/br_negativeData")
    public ResponseEntity<List<NegativeMaps>> getbrNegative() {
        // Base path to the Excel files
        String basePath = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\negative maps\\filtered_output_br.xlsx";
        // Construct the full path by appending the fileName parameter and file extension
//        String excelFilePath = basePath + fileName + "_Mixed_Map.xlsx";

        // Use the ExcelReader to read data from the Excel file
        List<NegativeMaps> dataList = excelReader.readNegativeMapData(basePath);

        // Return the list of Mix objects
        return ResponseEntity.ok(dataList);
    }

    @GetMapping("/up_negativeData")
    public ResponseEntity<List<NegativeMaps>> getupNegative() {
        // Base path to the Excel files
        String basePath = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\negative maps\\filtered_output_up.xlsx";
        // Construct the full path by appending the fileName parameter and file extension
//        String excelFilePath = basePath + fileName + "_Mixed_Map.xlsx";

        // Use the ExcelReader to read data from the Excel file
        List<NegativeMaps> dataList = excelReader.readNegativeMapData(basePath);

        // Return the list of Mix objects
        return ResponseEntity.ok(dataList);
    }

    @GetMapping("/ka_negativeData")
    public ResponseEntity<List<NegativeMaps>> getkaNegative() {
        // Base path to the Excel files
        String basePath = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\negative maps\\filtered_output_ka.xlsx";
        // Construct the full path by appending the fileName parameter and file extension
//        String excelFilePath = basePath + fileName + "_Mixed_Map.xlsx";

        // Use the ExcelReader to read data from the Excel file
        List<NegativeMaps> dataList = excelReader.readNegativeMapData(basePath);

        // Return the list of Mix objects
        return ResponseEntity.ok(dataList);
    }


    //
    @PostMapping("/api/runPythonScripts")
    public ResponseEntity<String> runPythonScripts() {
        try {
            System.out.println("front end req i got");
            String line;
            ProcessBuilder processBuilder = new ProcessBuilder("C:\\Users\\Teja\\AppData\\Local\\Programs\\Python\\Python312\\python.exe",
                    "C:\\Users\\Teja\\Desktop\\karthik\\demo\\All_codes\\Combined_code_village.py");
            processBuilder.redirectErrorStream(true); // Redirects error stream to standard output
            Process process = processBuilder.start();

            StringBuilder output = new StringBuilder();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));

            while ((line = reader.readLine()) != null) {
                output.append(line + "\n");
            }

            int exitCode = process.waitFor();
            if (exitCode == 0) {
                return ResponseEntity.ok(output.toString());
            } else {
                return ResponseEntity.badRequest().body("Script execution failed with errors: " + output.toString());
            }
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body("Server error: " + e.getMessage());
        }
    }
//    private static final String PYTHON_EXECUTABLE = "C:\\Users\\Teja\\AppData\\Local\\Programs\\Python\\Python312\\python.exe";
//    private static final String SCRIPTS_BASE_PATH = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\All_codes\\";
//    @PostMapping("/api/runPythonScripts")
//    public ResponseEntity<String> runPythonScripts() {
//        try {
//            System.out.println("Front end request received");
//// Run the first.py script first
//            String firstScriptOutput = runScript("first.py");
//            System.out.println("first.py Output:\n" + firstScriptOutput);
//            // List of Python scripts in category 1
//            List<String> category1Scripts = Arrays.asList(
//                    "Village_detail_2.py",
//                    "add_Tru.py",
//                    "excel_cleaning_village.py",
//                    "Cat_Status.py",
//                    "test.py",
//                    "branch_name_from_bcode.py",
//                    "village_state-hits.py",
//                    "Branch_village_count.py",
//                    "censuscode_merge_village.py",
//                    "merge_excel.py"
//            );
//
//            // List of Python scripts in category 2
//            List<String> category2Scripts = Arrays.asList(
//                    "Center_details_2.py",
//                    "add_Tru_center.py",
//                    "excel_cleaning.py",
//                    "cat_st_center.py",
//                    "CENTERCOUNT.py",
//                    "all_center.py",
//                    "Bcode_from_BName.py",
//                    "Center_state_hits.py",
//                    "loan_appl.py",
//                    "Center_last.py",
//                    "censuscode_merge_center.py",
//                    "center_village_count.py",
//                    "Center_state_hits.py",
//                    "merge_center.py"
//            );
//
//            // List of Python scripts in category 3
//            List<String> category3Scripts = Arrays.asList(
//                    "Merge_final.py",
//                    "final_mix.py",
//                    "centermix.py",
//                    "xx.py"
//            );
//
//            // Create a thread pool to run categories 1 and 2 in parallel
//            ExecutorService executorService = Executors.newFixedThreadPool(2);
//
//            // Submit tasks to run categories 1 and 2 sequentially but in parallel with each other
//            Future<String> category1Future = executorService.submit(() -> runScriptsSequentially(category1Scripts));
//            Future<String> category2Future = executorService.submit(() -> runScriptsSequentially(category2Scripts));
//
//            // Collect the results of categories 1 and 2
//            StringBuilder output = new StringBuilder();
//            output.append("Category 1 Output:\n").append(category1Future.get()).append("\n");
//            output.append("Category 2 Output:\n").append(category2Future.get()).append("\n");
//
//            // Run category 3 scripts sequentially after categories 1 and 2 are complete
//            output.append("Category 3 Output:\n").append(runScriptsSequentially(category3Scripts)).append("\n");
//
//            // Shutdown the executor service
//            executorService.shutdown();
//
//            return ResponseEntity.ok(output.toString());
//        } catch (Exception e) {
//            return ResponseEntity.internalServerError().body("Server error: " + e.getMessage());
//        }
//    }
//
//    @NotNull
//    private String runScriptsSequentially(@NotNull List<String> scripts) throws Exception {
//        StringBuilder output = new StringBuilder();
//        for (String script : scripts) {
//            output.append(runScript(script)).append("\n");
//        }
//        return output.toString();
//    }
//
//    @NotNull
//    private String runScript(@NotNull String scriptName) throws Exception {
//        ProcessBuilder processBuilder = new ProcessBuilder(
//                PYTHON_EXECUTABLE,
//                SCRIPTS_BASE_PATH + scriptName
//        );
//        processBuilder.redirectErrorStream(true); // Redirects error stream to standard output
//        Process process = processBuilder.start();
//
//        StringBuilder output = new StringBuilder();
//        try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
//            String line;
//            while ((line = reader.readLine()) != null) {
//                output.append(line).append("\n");
//            }
//        }
//
//        int exitCode = process.waitFor();
//        if (exitCode != 0) {
//            throw new Exception("Script " + scriptName + " execution failed with exit code " + exitCode);
//        }
//
//        return output.toString();
//    }
}
