package com.example.demo;

import org.springframework.data.jpa.repository.Query;
import java.util.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.data.repository.query.Param;
@Repository
public interface UserRepository extends JpaRepository<User_s, Long> {
    List<User_s> findAllByOrderByEpochDataAsc();
    Page<User_s> findByDeviceId(String deviceId, Pageable pageable);
    Page<User_s> findByDeviceIdAndEpochDataBetween(String deviceId, Long startEpoch, Long endEpoch, Pageable pageable);
    @Query(value = "SELECT \n" +
            "    d.device_id, \n" +
            "    COUNT(d.device_id),\n" +
            "    SUM(d.speed),\n" +
            "    SUM(d.delta_t),\n" +
            "    SUM(d.delta_distance),\n" +
            "    SUM(d.mov_avg_spd),\n" +
            "    MIN(CONVERT(datetime, DATEADD(SECOND, d.epoch_data / 1000, '1970-01-01 00:00:00'))) AS start_date,\n" +
            "    MAX(CONVERT(datetime, DATEADD(SECOND, d.epoch_data / 1000, '1970-01-01 00:00:00'))) AS end_date\n" +
            "FROM \n" +
            "    ts d \n" +
            "GROUP BY \n" +
            "    d.device_id\n", nativeQuery = true)
    List<Object[]> getDeviceIdCountsSumsAndMinMaxHumanReadableDatesAndDiff();

    @Query("SELECT u.epochData FROM User_s u")
    Set<Long> findAllEpochData();

    //  @Query(value = "SELECT SUM(d.delta_distance) FROM ts d WHERE d.device_id = :deviceId AND d.epoch_data BETWEEN :startEpoch AND :endEpoch", nativeQuery = true)
//     Double findTotalDistanceByDeviceIdAndEpochDataBetween(@Param("deviceId") String deviceId, @Param("startEpoch") Long startEpoch, @Param("endEpoch") Long endEpoch);
    // @Query(value = "SELECT SUM(d.delta_distance) FROM ts d WHERE d.device_id = :deviceId AND d.epoch_data BETWEEN :startEpoch AND :endEpoch AND d.speed>10 && d.speed <= 65", nativeQuery = true)
    // Double findTotalDistanceByDeviceIdAndEpochDataBetween(@Param("deviceId") String deviceId, @Param("startEpoch") Long startEpoch, @Param("endEpoch") Long endEpoch);
    @Query(value = "SELECT SUM(d.delta_distance) FROM ts d WHERE d.device_id = :deviceId AND d.epoch_data BETWEEN :startEpoch AND :endEpoch", nativeQuery = true)
    Double findTotalDistanceByDeviceIdAndEpochDataBetween(@Param("deviceId") String deviceId, @Param("startEpoch") Long startEpoch, @Param("endEpoch") Long endEpoch);


}
