package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Stage 
* Discrete step (stage) of device activity (such as heating and cooling outputs).
*/
@SuppressWarnings("serial")
public class Stage extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IStage{

	IRI newInstance;
	public Stage(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Stage"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IStage> getAllStagesObjectsCreated(){
		Set<IStage> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Stage")).subjects().stream()
		.map(mapper->(IStage)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}