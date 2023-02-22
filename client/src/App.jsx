import { useState } from 'react'
import {
  ChakraProvider,
  Heading,
  Container,
  Text,
  Input,
  Button,
  Wrap,
  Stack, 
  Image,
  Link,
  SkeletonCircle,
  SkeletonText,
} from "@chakra-ui/react";
import axios from "axios";

function App() {
  const [image, setImage] = useState();
  const [prompt, setPrompt] = useState();
  const [loading, setLoader] = useState();

  const generate = async (prompt) => {
    setLoader(true);
    const result = await axios.get(`http://localhost:8000/?prompt=${prompt}`);

    console.log('result', result);

    // check response is 200
    if ( result.status === 200 ) {
      setImage(result.data);
    } else {
      alert("Error generating image, please try again");
    }

    setLoader(false);
  };

  return (
    <ChakraProvider>
      <Container>
        <Heading>Stable DIffusion Interface</Heading>
        <Text marginBottom={"10px"}>
          Using stable-diffusion-v1-4{" "}
          <Link href={"https://huggingface.co/CompVis/stable-diffusion-v1-4"}>
            Link
          </Link>
        </Text>

        <Wrap marginBottom={"10px"}>
          <Input
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            width={"400px"}
            placeholder="a photo of an astronaut riding a horse on mars"
          ></Input>
          <Button onClick={(e) => generate(prompt)} colorScheme={"yellow"}>
            Generate Image
          </Button>
        </Wrap>

        {loading ? (
          <Stack>
            <SkeletonCircle />
            <SkeletonText />
          </Stack>
        ) : image ? (
          <Image src={`data:image/png;base64,${image}`} boxShadow="lg" />
        ) : null}
      </Container>
    </ChakraProvider>
  );
}

export default App;
