
/** @jsxImportSource @emotion/react */import { Fragment } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, Center, Flex, Heading, HStack, Image as ChakraImage, Link, Spacer, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextLink from "next/link"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Box>
  <VStack sx={{"bg": "#212529", "position": "sticky", "borderBottom": "0.25em solid #D3D3D3", "paddingX": "2em", "paddingY": "1em", "zIndex": "999", "top": "0", "width": "100%"}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={` Imagen`} src={`mouredev.png`} sx={{"width": "4em", "heigth": "4em"}}/>
  <Text>
  {`CtrlJ - Desarrollador de Software`}
</Text>
  <Spacer/>
  <Link as={NextLink} className={`nes-icon youtube is-medium`} href={`https://www.youtube.com/@CtrlJDev`} isExternal={true} sx={{"textDecoration": "none", "_hover": {"color": "#EA5940", "textDecoration": "none"}}}>
  {``}
</Link>
  <Link as={NextLink} className={`nes-icon github is-medium`} href={`https://github.com/Javih95`} isExternal={true} sx={{"textDecoration": "none", "_hover": {"color": "#EA5940", "textDecoration": "none"}}}>
  {``}
</Link>
</HStack>
</VStack>
  <Center>
  <VStack spacing={`4em`} sx={{"width": "100%"}}>
  <VStack sx={{"alignItems": "start", "paddingX": "2em", "maxWidth": "1000px", "paddingTop": "4em"}}>
  <Heading size={`lg`} sx={{"paddingBottom": "1em", "fontFamily": "Press Start 2P", "color": "#EA5940"}}>
  {`Bienvenido a mi espacio digital`}
</Heading>
  <Flex sx={{"flexDirection": ["column", "column", "column", "row", "row"]}}>
  <ChakraImage alt={`Avatar`} src={`mouredev.png`} sx={{"width": "16em", "heigth": "16em", "marginRight": "2em"}}/>
  <VStack alignItems={`start`}>
  <Box>
  <Text>
  {`Soy CtrlJ,desarrollador de software`}
</Text>
  <Text>
  {`enfocado en la creación de soluciones innovadoras`}
</Text>
</Box>
  <Text as={`span`}>
  {`Explora `}
  <Text as={`span`} sx={{"color": "#EA5940"}}>
  {`mi portafolio`}
</Text>
  {` para descubrir proyectos emocionantes`}
</Text>
  <Text as={`span`}>
  {`conoce mis habilidades técnicas `}
</Text>
  <Text as={`span`}>
  {`y únete a mí en el viaje de la programación`}
</Text>
  <Link as={NextLink} href={`https://www.linkedin.com/in/javier-aguirre95`} isExternal={true} sx={{"color": "#D3D3D3", "paddinTop": "2em", "fontSize": "0.8em", "textDecoration": "none", "_hover": {"color": "#EA5940", "textDecoration": "none"}}}>
  {`linkedin`}
</Link>
</VStack>
</Flex>
</VStack>
  <HStack alignItems={`center`} sx={{"alignItems": "start", "paddingX": "2em", "maxWidth": "1000px", "paddingButtom": "2em"}}>
  <VStack spacing={`0.8em`} sx={{"alingItems": "start"}}>
  <Text sx={{"fontSize": "0.8em", "marginButton": "0.5em"}}>
  {`© 2023 CtrlJ. Todos los derechos reservados.`}
</Text>
  <Link as={NextLink} href={`https://www.linkedin.com/in/javier-aguirre95`} isExternal={true} sx={{"fontSize": "0.8em", "color": "#D3D3D3", "textDecoration": "none", "_hover": {"color": "#EA5940", "textDecoration": "none"}}}>
  {`CtrlJ - Desarrollador Web`}
</Link>
</VStack>
  <Spacer/>
  <ChakraImage alt={`logo`} className={`nes-avatar is-large`} src={`mouredev.png`}/>
</HStack>
</VStack>
</Center>
</Box>
  <NextHead>
  <title>
  {`CtrlJ - Desarrollador de Software`}
</title>
  <meta content={`Bienvenido a mi espacio digital, donde la creatividad y la pasión se encuentran con el código. Soy CtrlJ, un desarrollador de software con un enfoque único en la creación de soluciones innovadoras. Explora mi portafolio para descubrir proyectos emocionantes, conoce mis habilidades técnicas y únete a mí en el viaje de la programación. ¡Transformemos ideas en realidad!`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
