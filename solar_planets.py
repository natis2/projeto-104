import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )

cv2.putText(img,
            "Mercurio",
            (100,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,225)
            )

cv2.putText(img,
            "Venus",
            (200,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,225)
            )

cv2.putText(img,
            "Terra",
            (300,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,225)
            )

cv2.putText(img,
            "Marte",
            (370,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,225)
            )

cv2.putText(img,
            "Jupiter",
            (470,80),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,225)
            )

cv2.putText(img,
            "Saturno",
            (770,80),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,225)
            )

cv2.putText(img,
            "Urano",
            (970,80),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,225)
            )

cv2.putText(img,
            "Netuno",
            (1100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,225)
            )

cv2.imshow("resultado", img)

cv2.waitKey(0)