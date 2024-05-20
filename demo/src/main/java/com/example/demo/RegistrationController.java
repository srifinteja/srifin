//package com.example.demo;
//
////import com.genuinecoder.learnspringsecurity.model.MyUser;
////import com.genuinecoder.learnspringsecurity.model.MyUserRepository;
//import com.example.demo.model.MyUser;
//import com.example.demo.model.MyUserRepository;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.security.crypto.password.PasswordEncoder;
//import org.springframework.web.bind.annotation.PostMapping;
//import org.springframework.web.bind.annotation.RequestBody;
//import org.springframework.web.bind.annotation.RestController;
//
//@RestController
//public class RegistrationController {
//
//    @Autowired
//    private MyUserRepository myUserRepository;
//    @Autowired
//    private PasswordEncoder passwordEncoder;
//
//    @PostMapping("/register/user")
//    public MyUser createUser(@RequestBody MyUser user) {
//        user.setPassword(passwordEncoder.encode(uaser.getPassword()));
//        return myUserRepository.save(user);
//    }
//}