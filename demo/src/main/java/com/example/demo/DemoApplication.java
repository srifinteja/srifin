package com.example.demo;

import com.fasterxml.jackson.databind.ObjectMapper;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import java.time.*;
import java.io.IOException;
import java.util.ArrayList;
import java.util.*;
import java.time.temporal.ChronoUnit;
import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.TimeUnit;

		@SpringBootApplication
		public class DemoApplication {

			public static void main(String[] args) {
				SpringApplication.run(DemoApplication.class, args);
			}
			@Bean
			public CommandLineRunner commandLineRunner(DatabaseInserter databaseInserter, ObjectMapper objectMapper) {
				return args -> {
					databaseInserter.clearDatabase();
					List<String> deviceIds = fetchDeviceIds();
					// List<String> deviceIds = Arrays.asList("9740161211", "6394934198", "7905324311", "8171058530", "9473538088", "9076787184", "7272850869", "8953603550");
					// System.out.println(deviceIds);
					ExecutorService executor = Executors.newFixedThreadPool(10); // Use a thread pool to handle concurrent requests

					for (String deviceId : deviceIds) {
						executor.submit(() -> processDevice(deviceId, databaseInserter, objectMapper));
					}

					executor.shutdown();
					try {
						executor.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
					} catch (InterruptedException e) {
						Thread.currentThread().interrupt();
					}

					System.out.println("Finished fetching data.");
				};
			}

			private void processDevice(String deviceId, DatabaseInserter databaseInserter, ObjectMapper objectMapper) {
				int page = 1;
				final int rowsPerPage = 10000;
				boolean continueFetching = true;

				while (continueFetching) {
					try {
						String data = fetchGeoLocationData(page, rowsPerPage, deviceId);
						GeoLocationDataResponse response = objectMapper.readValue(data, GeoLocationDataResponse.class);

						if (response.hasRecords()) {
							databaseInserter.insertData(Collections.singletonList(data));
							System.out.println("Data for page " + page + " of device ID " + deviceId + " has been processed and inserted into the database.");
							page++;
						} else {
							continueFetching = false;
						}
					} catch (IOException e) {
						System.out.println("IOException occurred for device ID: " + deviceId + " at page " + page + ": " + e.getMessage());
						// Handle the exception, maybe retry or break
					}
					// catch (SocketTimeoutException e) {
					//     System.out.println("Timeout occurred for device ID: " + deviceId + " at page " + page);
					// } catch (JsonProcessingException e) {
					//     System.out.println("Error processing JSON data: " + e.getMessage());
					// }
				}
			}

			public static String fetchGeoLocationData(int page,int rows,String deviceId) throws IOException {
				String url = "https://gpslog.srifincredit.com/shrms/get_device_location";

				OkHttpClient client = new OkHttpClient();
				ObjectMapper objectMapper = new ObjectMapper(); // Jackson's ObjectMapper
				long currentTimeInSeconds = Instant.now().getEpochSecond();

				long previousDayTimeInSeconds = Instant.now().minus(2, ChronoUnit.DAYS).getEpochSecond();
				Map<String, Object> requestBodyMap = new HashMap<>();
				requestBodyMap.put("deviceID", deviceId);
				requestBodyMap.put("page", page);
				requestBodyMap.put("rows", rows);
				requestBodyMap.put("ts_from", previousDayTimeInSeconds);
				requestBodyMap.put("ts_to", currentTimeInSeconds);

				// Convert Map to JSON String
				String requestBodyJson = objectMapper.writeValueAsString(requestBodyMap);

				RequestBody requestBody = RequestBody.create(requestBodyJson, MediaType.get("application/json; charset=utf-8"));

				Request request = new Request.Builder()
						.url(url)
						.post(requestBody)
						.addHeader("X-API-TOKEN", "TLQ6lMV3RxujZBhOyKbkcWftANEvPawJgrm0nSXG1UdIeoq5p2")
						.addHeader("Accept", "application/json")
						.build();

				try (Response response = client.newCall(request).execute()) {
					if (!response.isSuccessful()) throw new IOException("Unexpected code " + response);

					return response.body().string();
				}
			}
			public static List<String> fetchDeviceIds() throws IOException {
				String apiUrl = "https://gpslog.srifincredit.com/shrms/get_device_ids";
				OkHttpClient client = new OkHttpClient();
				Request request = new Request.Builder()
						.url(apiUrl)
						.get()
						.addHeader("X-API-TOKEN", "TLQ6lMV3RxujZBhOyKbkcWftANEvPawJgrm0nSXG1UdIeoq5p2")
						.addHeader("Accept", "application/json")
						.build();

				try (Response okhttpResponse = client.newCall(request).execute()) {
					if (!okhttpResponse.isSuccessful()) throw new IOException("Unexpected code " + okhttpResponse);

					ObjectMapper objectMapper = new ObjectMapper();
					DeviceIdApiResponse response = objectMapper.readValue(okhttpResponse.body().string(), DeviceIdApiResponse.class);

					// Extract device IDs from the records
					List<String> deviceIds = new ArrayList<>();
					for (DeviceRecord record : response.getRecords()) {
						deviceIds.add(record.getDeviceid());
					}
					return deviceIds;
				}
			}



//			@Bean
//			public CommandLineRunner demo(ExcelReader excelReader) {
//				return (args) -> {
//					String excelFilePath = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\Shivpur_Tracked.xlsx";
//					List<CensusData> dataList = excelReader.readExcelFile(excelFilePath);
//					// Assuming you have a toString method in CensusData or use logger to print
////					dataList.forEach(data -> System.out.println(data));
//					// Or use a logger to log the data
//				};
//			}
//
//			@Bean
//			public CommandLineRunner under15DataDemo(ExcelReader excelReader) {
//				return (args) -> {
//					String excelFilePath = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\BR_Surroundings\\Shivpur_15_km.xlsx";
//					List<Under15> under15DataList = excelReader.readUnder15Data(excelFilePath);
////					under15DataList.forEach(data -> System.out.println(data));
//				};
//			}
//			@Bean
//			public CommandLineRunner combinedData(ExcelReader excelReader) {
//				return (args) -> {
//					String excelFilePath = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\combined_file (2).xlsx";
//					List<Combined> combinedList = excelReader.combinedData(excelFilePath);
////					combinedList.forEach(data -> System.out.println(data));
//				};
//			}


			@Bean
			public CommandLineRunner mapData(ExcelReader excelReader) {
				return (args) -> {
					String excelFilePath = "app/radar/up_data.xlsx";
					List<Mapdata> combinedList = excelReader.readLocationData(excelFilePath);
//					combinedList.forEach(data -> System.out.println(data));
				};
			}
//			@Bean
//			public CommandLineRunner mixData(ExcelReader excelReader) {
//				return (args) -> {
//					String excelFilePath = "C:\\Users\\Teja\\Desktop\\karthik\\demo\\mixedd\\Belagavi_Mixed_Map.xlsx";
//					List<Mix> combinedList = excelReader.readMapData(excelFilePath);
////					combinedList.forEach(data -> System.out.println(data));
//				};
//			}
			@Bean
			public ExcelReader excelReader() {
				return new ExcelReader();
			}
		}



