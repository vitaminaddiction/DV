package com.visual.dv.DVWeb.menu;


import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.Resource;
import org.springframework.core.io.UrlResource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.util.UriUtils;

import java.net.MalformedURLException;
import java.nio.charset.StandardCharsets;

@Controller
@RequestMapping("menu")
public class MenuController {

    @Value("${file.upload.path}")
    private String uploadPath;

    @GetMapping("menu1")
    public String menu1(){
        return "menu/menu1";
    }

    @GetMapping("menu2")
    public String menu2(){
        return "menu/menu2";
    }

    @GetMapping("menu3")
    public String menu3(){
        return "menu/menu3";
    }

    @GetMapping("menu4")
    public String menu4(){
        return "menu/menu4";
    }

    @GetMapping("menu5")
    public String menu5(){
        return "menu/menu5";
    }

    @GetMapping("/attach/{filename}")
    public ResponseEntity<Resource> downloadAttach(@PathVariable String filename)
            throws MalformedURLException {

//        FileEntity file = fileRepository.findById(id).orElse(null);

        UrlResource resource = new UrlResource("file:" + uploadPath+"/"+filename);

        String encodedFileName = UriUtils.encode(filename, StandardCharsets.UTF_8);

        // 파일 다운로드 대화상자가 뜨도록 하는 헤더를 설정해주는 것
        // Content-Disposition 헤더에 attachment; filename="업로드 파일명" 값을 준다.
        String contentDisposition = "attachment; filename=\"" + encodedFileName + "\"";

        return ResponseEntity.ok().header(HttpHeaders.CONTENT_DISPOSITION,contentDisposition).body(resource);
    }
}
