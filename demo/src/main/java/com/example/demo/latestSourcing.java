package com.example.demo;

public class latestSourcing {


    private Long censuscode2011;
    private String village;
    private String pincode;
    private String district;
    private String state;
    private Integer population;
    private Integer houseHolds;
    private String ur; // Assuming this is a String, change as necessary
    private Double latMinBoundCentroid;

    public Long getCensuscode2011() {
        return censuscode2011;
    }

    public void setCensuscode2011(Long censuscode2011) {
        this.censuscode2011 = censuscode2011;
    }

    public String getVillage() {
        return village;
    }

    public void setVillage(String village) {
        this.village = village;
    }

    public String getPincode() {
        return pincode;
    }

    public void setPincode(String pincode) {
        this.pincode = pincode;
    }

    public String getDistrict() {
        return district;
    }

    public void setDistrict(String district) {
        this.district = district;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public Integer getPopulation() {
        return population;
    }

    public void setPopulation(Integer population) {
        this.population = population;
    }

    public Integer getHouseHolds() {
        return houseHolds;
    }

    public void setHouseHolds(Integer houseHolds) {
        this.houseHolds = houseHolds;
    }

    public String getUr() {
        return ur;
    }

    public void setUr(String ur) {
        this.ur = ur;
    }

    public Double getLatMinBoundCentroid() {
        return latMinBoundCentroid;
    }

    public void setLatMinBoundCentroid(Double latMinBoundCentroid) {
        this.latMinBoundCentroid = latMinBoundCentroid;
    }

    public Double getLongMinBoundCentroid() {
        return longMinBoundCentroid;
    }

    public void setLongMinBoundCentroid(Double longMinBoundCentroid) {
        this.longMinBoundCentroid = longMinBoundCentroid;
    }

    public String getJun23Cat() {
        return jun23Cat;
    }

    public void setJun23Cat(String jun23Cat) {
        this.jun23Cat = jun23Cat;
    }

    public String getVisited() {
        return visited;
    }

    public void setVisited(String visited) {
        this.visited = visited;
    }

    private Double longMinBoundCentroid;
    private String jun23Cat;
    private String visited;
    @Override
    public String toString() {
        return "VillageDetail{" +
                "censuscode2011=" + censuscode2011 +
                ", village='" + village + '\'' +
                ", pincode=" + pincode +
                ", district='" + district + '\'' +
                ", state='" + state + '\'' +
                ", population=" + population +
                ", houseHolds=" + houseHolds +
                ", ur='" + ur + '\'' +
                ", latMinBoundCentroid=" + latMinBoundCentroid +
                ", longMinBoundCentroid=" + longMinBoundCentroid +
                ", jun23Cat='" + jun23Cat + '\'' +
                ", visited=" + visited +
                '}';
    }

}
