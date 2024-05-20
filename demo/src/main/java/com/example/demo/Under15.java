package com.example.demo;

public class Under15 {
        private String censuscode2011;
        private String village;
        private String pincode;
        private String district;
        private String state;
        private int tot_p_2011;
        private int no_hh_2011;

    public String getCensuscode2011() {
        return censuscode2011;
    }

    public void setCensuscode2011(String censuscode2011) {
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

    public int getTot_p_2011() {
        return tot_p_2011;
    }

    public void setTot_p_2011(int tot_p_2011) {
        this.tot_p_2011 = tot_p_2011;
    }

    public int getNo_hh_2011() {
        return no_hh_2011;
    }

    public void setNo_hh_2011(int no_hh_2011) {
        this.no_hh_2011 = no_hh_2011;
    }

    public String getTru_2011() {
        return tru_2011;
    }

    public void setTru_2011(String tru_2011) {
        this.tru_2011 = tru_2011;
    }

    public boolean getIs_pc_in() {
        return is_pc_in;
    }

    public void setIs_pc_in(boolean is_pc_in) {
        this.is_pc_in = is_pc_in;
    }

    public double getLat_min_bound_centroid() {
        return lat_min_bound_centroid;
    }

    public void setLat_min_bound_centroid(double lat_min_bound_centroid) {
        this.lat_min_bound_centroid = lat_min_bound_centroid;
    }

    public double getLong_min_bound_centroid() {
        return long_min_bound_centroid;
    }

    public void setLong_min_bound_centroid(double long_min_bound_centroid) {
        this.long_min_bound_centroid = long_min_bound_centroid;
    }

    public String getAlpha_70_stat() {
        return alpha_70_stat;
    }

    public void setAlpha_70_stat(String alpha_70_stat) {
        this.alpha_70_stat = alpha_70_stat;
    }

    public boolean getPoly_valid() {
        return poly_valid;
    }

    public void setPoly_valid(boolean poly_valid) {
        this.poly_valid = poly_valid;
    }

    public String getFinal_cat() {
        return final_cat;
    }

    public void setFinal_cat(String final_cat) {
        this.final_cat = final_cat;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getDeep_stat() {
        return deep_stat;
    }

    public void setDeep_stat(String deep_stat) {
        this.deep_stat = deep_stat;
    }

    public String getDeep_status() {
        return deep_status;
    }

    public void setDeep_status(String deep_status) {
        this.deep_status = deep_status;
    }

    public String getB_dist() {
        return b_dist;
    }

    public void setB_dist(String b_dist) {
        this.b_dist = b_dist;
    }

    private String tru_2011;
        private boolean is_pc_in;
        private double lat_min_bound_centroid;
        private double long_min_bound_centroid;
        private String alpha_70_stat;
        private boolean poly_valid;
        private String final_cat;
        private String status;
        private String deep_stat;
        private String deep_status;
        private String b_dist;

        // Constructor, getters, and setters
        // Constructor
        public Under15() {
        }

    @Override
    public String toString() {
        return "Under15{" +
                "censuscode2011='" + censuscode2011 + '\'' +
                ", village='" + village + '\'' +
                ", pincode='" + pincode + '\'' +
                ", district='" + district + '\'' +
                ", state='" + state + '\'' +
                ", tot_p_2011=" + tot_p_2011 +
                ", no_hh_2011=" + no_hh_2011 +
                ", tru_2011=" + tru_2011 +
                ", is_pc_in='" + is_pc_in + '\'' +
                ", lat_min_bound_centroid=" + lat_min_bound_centroid +
                ", long_min_bound_centroid=" + long_min_bound_centroid +
                ", alpha_70_stat='" + alpha_70_stat + '\'' +
                ", poly_valid='" + poly_valid + '\'' +
                ", final_cat='" + final_cat + '\'' +
                ", status='" + status + '\'' +
                ", deep_stat='" + deep_stat + '\'' +
                ", deep_status='" + deep_status + '\'' +
                ", b_dist='" + b_dist + '\'' +
                '}';
    }





}
