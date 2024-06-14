package com.example.demo;

import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.File;
import java.io.FileInputStream;
import java.util.*;

import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.File;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class ExcelReader {

    public List<CensusData> readExcelFile(String excelFilePath) {
        List<CensusData> dataList = new ArrayList<>();
        try (FileInputStream excelFile = new FileInputStream(new File(excelFilePath))) {
            Workbook workbook = new XSSFWorkbook(excelFile);
            Sheet datatypeSheet = workbook.getSheetAt(0);
            Iterator<Row> iterator = datatypeSheet.iterator();

            // Skip header
            if (iterator.hasNext()) {
                iterator.next();
            }

            while (iterator.hasNext()) {
                Row currentRow = iterator.next();
                CensusData data = new CensusData();

                // Read and set data for each field using utility methods
                data.setCensusCode2011(getCellStringValue(currentRow.getCell(0)));
                data.setVillage(getCellStringValue(currentRow.getCell(1)));
                data.setPincode(getCellStringValue(currentRow.getCell(2)));
                data.setDistrict(getCellStringValue(currentRow.getCell(3)));
                data.setState(getCellStringValue(currentRow.getCell(4)));
                data.setTotP2011((long) getCellNumericValue(currentRow.getCell(5)));
                // Handling optional numeric value with null check
                Cell noHh2011Cell = currentRow.getCell(6);
                if (noHh2011Cell != null && noHh2011Cell.getCellType() == CellType.NUMERIC) {
                    data.setNoHh2011((long) noHh2011Cell.getNumericCellValue());
                }
                data.setTru2011(getCellStringValue(currentRow.getCell(7)));
                data.setLatMinBoundCentroid(getCellNumericValue(currentRow.getCell(8)));
                data.setLongMinBoundCentroid(getCellNumericValue(currentRow.getCell(9)));
                data.setFinalCat(getCellStringValue(currentRow.getCell(10)));
                data.setStatus(getCellStringValue(currentRow.getCell(11)));
                data.setDeepStatus(getCellStringValue(currentRow.getCell(12)));
                data.setbDist(getCellNumericValue(currentRow.getCell(13)));
                data.setVisited(getCellStringValue(currentRow.getCell(14)));

                dataList.add(data);
            }
        } catch (Exception e) {
            e.printStackTrace(); // Consider replacing with a logger
        }
        return dataList;
    }



    public List<Under15> readUnder15Data(String excelFilePath) {
        List<Under15> dataList = new ArrayList<>();
        try (FileInputStream excelFile = new FileInputStream(new File(excelFilePath))) {
            Workbook workbook = new XSSFWorkbook(excelFile);
            Sheet datatypeSheet = workbook.getSheetAt(0);
            Iterator<Row> iterator = datatypeSheet.iterator();

            // Skip header
            if (iterator.hasNext()) {
                iterator.next();
            }

            while (iterator.hasNext()) {
                Row currentRow = iterator.next();
                Under15 data = new Under15();

                // Read and set data for each field using utility methods
                data.setCensuscode2011(getCellStringValue(currentRow.getCell(0)));
                data.setVillage(getCellStringValue(currentRow.getCell(1)));
                data.setPincode(getCellStringValue(currentRow.getCell(2)));
                data.setDistrict(getCellStringValue(currentRow.getCell(3)));
                data.setState(getCellStringValue(currentRow.getCell(4)));
                data.setTot_p_2011((int) getCellNumericValue(currentRow.getCell(5)));
                data.setNo_hh_2011((int) getCellNumericValue(currentRow.getCell(6)));
                data.setTru_2011(getCellStringValue(currentRow.getCell(7)));
                data.setIs_pc_in(getCellBooleanValue(currentRow.getCell(8)));
//                System.out.println(getCellBooleanValue(currentRow.getCell(8)));
                data.setLat_min_bound_centroid(getCellNumericValue(currentRow.getCell(9)));
                data.setLong_min_bound_centroid(getCellNumericValue(currentRow.getCell(10)));
                data.setAlpha_70_stat(getCellStringValue(currentRow.getCell(11)));
                data.setPoly_valid(getCellBooleanValue(currentRow.getCell(12)));
                data.setFinal_cat(getCellStringValue(currentRow.getCell(13)));
                data.setStatus(getCellStringValue(currentRow.getCell(14)));
                data.setDeep_stat(getCellStringValue(currentRow.getCell(15)));
                data.setDeep_status(getCellStringValue(currentRow.getCell(16)));
                data.setB_dist(getCellStringValue(currentRow.getCell(17)));

                dataList.add(data);
            }
        } catch (Exception e) {
            e.printStackTrace(); // Consider replacing with a logger
        }
        return dataList;
    }

    public List<Combined> combinedData(String excelFilePath) {
        List<Combined> dataList = new ArrayList<>();
        try (FileInputStream excelFile = new FileInputStream(new File(excelFilePath))) {
            Workbook workbook = new XSSFWorkbook(excelFile);
            Sheet datatypeSheet = workbook.getSheetAt(0);
            Iterator<Row> iterator = datatypeSheet.iterator();

            // Skip header
            if (iterator.hasNext()) {
                iterator.next();
            }

            while (iterator.hasNext()) {
                Row currentRow = iterator.next();
                Combined data = new Combined();

                // Read and set data for each field using utility methods
                data.setCensusCode2011(getCellStringValue(currentRow.getCell(0)));
                data.setVillage(getCellStringValue(currentRow.getCell(1)));
                data.setPincode(getCellStringValue(currentRow.getCell(2)));
                data.setDistrict(getCellStringValue(currentRow.getCell(3)));
                data.setState(getCellStringValue(currentRow.getCell(4)));
                data.setTotP2011((int) getCellNumericValue(currentRow.getCell(5)));
                data.setNoHh2011((int) getCellNumericValue(currentRow.getCell(6)));
                data.setTru2011(getCellStringValue(currentRow.getCell(7)));
                data.setIsPcIn(getCellStringValue(currentRow.getCell(8)));
                data.setLatMinBoundCentroid(getCellNumericValue(currentRow.getCell(9)));
                data.setLongMinBoundCentroid(getCellNumericValue(currentRow.getCell(10)));
                data.setAlpha70Stat(getCellStringValue(currentRow.getCell(11)));
                data.setPolyValid(getCellStringValue(currentRow.getCell(12)));
                data.setFinalCat(getCellStringValue(currentRow.getCell(13)));
                data.setStatus(getCellStringValue(currentRow.getCell(14)));
                data.setDeepStat(getCellStringValue(currentRow.getCell(15)));
                data.setDeepStatus(getCellStringValue(currentRow.getCell(16)));
                data.setbDist(getCellNumericValue(currentRow.getCell(17)));
                data.setVisited(getCellStringValue(currentRow.getCell(18)));
                data.setCenter(getCellStringValue(currentRow.getCell(19)));

                // Add the populated object to the list
                dataList.add(data);
            }
        } catch (Exception e) {
            e.printStackTrace(); // Consider replacing with a logger
        }
        return dataList;
    }

    public List<Mapdata> readLocationData(String excelFilePath) {
        List<Mapdata> dataList = new ArrayList<>();
        try (FileInputStream excelFile = new FileInputStream(new File(excelFilePath))) {
            Workbook workbook = new XSSFWorkbook(excelFile);
            Sheet sheet = workbook.getSheetAt(0);
            Iterator<Row> iterator = sheet.iterator();

            // Skip header
            if (iterator.hasNext()) {
                iterator.next();
            }

            while (iterator.hasNext()) {
                Row currentRow = iterator.next();
                Mapdata mapdata = new Mapdata();

                // Read and set data for each field
                mapdata.setLatitude(getCellNumericValue(currentRow.getCell(0)));
                mapdata.setLongitude(getCellNumericValue(currentRow.getCell(1)));
                mapdata.setCreatedAt(getCellDateValue(currentRow.getCell(2)));
                mapdata.setUpdatedAt(getCellDateValue(currentRow.getCell(3)));
                mapdata.setFlag(getCellStringValue(currentRow.getCell(4)));

                // Add the populated object to the list
                dataList.add(mapdata);
            }
        } catch (Exception e) {
            e.printStackTrace(); // Consider replacing with a logger
        }
        return dataList;
    }

    public List<latestSourcing> readLatestSourcing(String excelFilePath) {
        List<latestSourcing> dataList = new ArrayList<>();
        try (FileInputStream excelFile = new FileInputStream(new File(excelFilePath))) {
            Workbook workbook = new XSSFWorkbook(excelFile);
            Sheet sheet = workbook.getSheetAt(0);
            Iterator<Row> iterator = sheet.iterator();

            // Skip header
            if (iterator.hasNext()) {
                iterator.next();
            }

            while (iterator.hasNext()) {
                Row currentRow = iterator.next();
                latestSourcing villageDetail = new latestSourcing();

                // Assuming specific cell indexes for each field based on your initial data structure
                villageDetail.setCensuscode2011((long) getCellNumericValue(currentRow.getCell(0)));
                villageDetail.setVillage(getCellStringValue(currentRow.getCell(1)));
                villageDetail.setPincode( getCellStringValue(currentRow.getCell(2)));
                villageDetail.setDistrict(getCellStringValue(currentRow.getCell(3)));
                villageDetail.setState(getCellStringValue(currentRow.getCell(4)));
                villageDetail.setPopulation((int) getCellNumericValue(currentRow.getCell(5)));
                villageDetail.setHouseHolds((int) getCellNumericValue(currentRow.getCell(6)));
                villageDetail.setUr(getCellStringValue(currentRow.getCell(7)));
                villageDetail.setLatMinBoundCentroid(getCellNumericValue(currentRow.getCell(8)));
                villageDetail.setLongMinBoundCentroid(getCellNumericValue(currentRow.getCell(9)));
                villageDetail.setJun23Cat(getCellStringValue(currentRow.getCell(10)));
                villageDetail.setVisited(getCellStringValue(currentRow.getCell(11)));

                // Add the populated object to the list
                dataList.add(villageDetail);
            }
        } catch (Exception e) {
            e.printStackTrace(); // Consider replacing with a logger
        }
        return dataList;
    }

public List<NegativeMaps> readNegativeMapData(String excelFilePath) {
    List<NegativeMaps> data = new ArrayList<>();
    try (FileInputStream excelFile = new FileInputStream(new File(excelFilePath))) {
        Workbook workbook = new XSSFWorkbook(excelFile);
        Sheet sheet = workbook.getSheetAt(0);
        Iterator<Row> iterator = sheet.iterator();

        // Skip header
        if (iterator.hasNext()) {
            iterator.next();
        }
        while (iterator.hasNext()) {
            Row currentRow = iterator.next();
            NegativeMaps negativeData = new NegativeMaps();
            negativeData.setBranch((String) getCellStringValue(currentRow.getCell(0)));
            negativeData.setLatestApplication((String) getCellStringValue(currentRow.getCell(1)));
            negativeData.setPincode((String) getCellStringValue(currentRow.getCell(2)));
            negativeData.setJun23Cat((String) getCellStringValue(currentRow.getCell(3)));
            negativeData.setRecordedPincode((String) getCellStringValue(currentRow.getCell(4)));
            negativeData.setRecordedPincodeCat((String) getCellStringValue(currentRow.getCell(5)));
            negativeData.setCensuscode2011((long)getCellNumericValue(currentRow.getCell(6)));
            negativeData.setVillage((String) getCellStringValue(currentRow.getCell(7)));
            negativeData.setDistrict((String) getCellStringValue(currentRow.getCell(8)));
            negativeData.setState((String) getCellStringValue(currentRow.getCell(9)));
            negativeData.setUr((String) getCellStringValue(currentRow.getCell(10)));
            negativeData.setInitiatedCen((String) getCellStringValue(currentRow.getCell(11)));
            negativeData.setCgt1Cen((String) getCellStringValue(currentRow.getCell(12)));
            negativeData.setCgt2Cen((String) getCellStringValue(currentRow.getCell(13)));
            negativeData.setGrtCen((String) getCellStringValue(currentRow.getCell(14)));
            negativeData.setActiveCen((String) getCellStringValue(currentRow.getCell(15)));
            negativeData.setLoanApps(getCellIntegerValue(currentRow.getCell(16)));
            negativeData.setCbFail(getCellIntegerValue(currentRow.getCell(17)));
            negativeData.setCbDone(getCellIntegerValue(currentRow.getCell(18)));
            negativeData.setCgt1(getCellIntegerValue(currentRow.getCell(19)));
            negativeData.setCgt2(getCellIntegerValue(currentRow.getCell(20)));
            negativeData.setGrt(getCellIntegerValue(currentRow.getCell(21)));
            negativeData.setDisbursed(getCellIntegerValue(currentRow.getCell(22))); // Example index, replace with the correct one
data.add(negativeData);

        }
    }
    catch (Exception e) {
        e.printStackTrace(); // Consider replacing with more robust error handling
    }
    return data;
}
    public List<Mix> readMapData(String excelFilePath) {
        List<Mix> dataList = new ArrayList<>();
        try (FileInputStream excelFile = new FileInputStream(new File(excelFilePath))) {
            Workbook workbook = new XSSFWorkbook(excelFile);
            Sheet sheet = workbook.getSheetAt(0);
            Iterator<Row> iterator = sheet.iterator();

            // Skip header
            if (iterator.hasNext()) {
                iterator.next();
            }

            while (iterator.hasNext()) {
                Row currentRow = iterator.next();
                Mix censusData = new Mix();

                // Populate the CensusData object with row data
                censusData.setCensuscode2011((int) getCellNumericValue(currentRow.getCell(0)));
                censusData.setVillage(getCellStringValue(currentRow.getCell(1)));
                censusData.setPincode(getCellStringValue(currentRow.getCell(2)));
                censusData.setDistrict(getCellStringValue(currentRow.getCell(3)));
                censusData.setPopulation((int) getCellNumericValue(currentRow.getCell(4)));
                censusData.setHouseHolds((int) getCellNumericValue(currentRow.getCell(5)));
                censusData.setUr(getCellStringValue(currentRow.getCell(6)));
                censusData.setLatMinBoundCentroid(getCellNumericValue(currentRow.getCell(7)));
                censusData.setLongMinBoundCentroid(getCellNumericValue(currentRow.getCell(8)));
                censusData.setJun23Cat(getCellStringValue(currentRow.getCell(9)));
                censusData.setCenterCount((int) getCellNumericValue(currentRow.getCell(10)));
                censusData.setInitiatedCen((int) getCellNumericValue(currentRow.getCell(11)));
                censusData.setCgt1Cen((int) getCellNumericValue(currentRow.getCell(12)));
                censusData.setCgt2Cen((int) getCellNumericValue(currentRow.getCell(13)));
                censusData.setGrtCen((int) getCellNumericValue(currentRow.getCell(14)));
                censusData.setActiveCen((int) getCellNumericValue(currentRow.getCell(15)));
                censusData.setLoanApps((int) getCellNumericValue(currentRow.getCell(16)));
                censusData.setCbFail((int) getCellNumericValue(currentRow.getCell(17)));
                censusData.setCbDone((int) getCellNumericValue(currentRow.getCell(18)));
                censusData.setCgt1((int) getCellNumericValue(currentRow.getCell(19)));
                censusData.setCgt2((int) getCellNumericValue(currentRow.getCell(20)));
                censusData.setGrt((int) getCellNumericValue(currentRow.getCell(21)));
                censusData.setDisbursed((int) getCellNumericValue(currentRow.getCell(22)));
                censusData.setCenter((String) getCellStringValue(currentRow.getCell(23)));
                censusData.setState((String) getCellStringValue(currentRow.getCell(24)));
                censusData.setVisited((String) getCellStringValue(currentRow.getCell(25)));
                censusData.setBranch_Distance((String) getCellStringValue(currentRow.getCell(26)));
                censusData.setCatStatus((String) getCellStringValue(currentRow.getCell(27)));
                censusData.setKey((String) getCellStringValue(currentRow.getCell(28)));


                // Continue for other fields based on their Excel column indices

                // Add the populated CensusData object to the dataList
                dataList.add(censusData);
            }
        } catch (Exception e) {
            e.printStackTrace(); // Consider replacing with more robust error handling
        }
        return dataList;
    }




    private Date getCellDateValue(Cell cell) {
        if (cell == null) {
            return null;
        }
        return cell.getDateCellValue();
    }

    private Boolean getCellBooleanValue(Cell cell) {
        if (cell == null) {
            return null;
        }
        return cell.getBooleanCellValue();
    }



    private String getCellStringValue(Cell cell) {
        if (cell == null) return "";
        return switch (cell.getCellType()) {
            case STRING -> cell.getStringCellValue();
            case NUMERIC -> String.valueOf(cell.getNumericCellValue());
            default -> "";
        };
    }

    private double getCellNumericValue(Cell cell) {
        if (cell == null) return 0;
        return cell.getCellType() == CellType.NUMERIC ? cell.getNumericCellValue() : 0;
    }
    private Integer getCellIntegerValue(Cell cell) {
        if (cell == null || cell.getCellType() == CellType.BLANK) {
            return null; // or return 0, depending on how you wish to handle blanks
        } else if (cell.getCellType() == CellType.NUMERIC) {
            return (int) cell.getNumericCellValue();
        } else {
            throw new IllegalArgumentException("Cell must be NUMERIC type");
        }
    }


}
