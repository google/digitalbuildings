package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Run 
* State of being active or operating. By default applies to control program for system (eg VAV program run_command).
*/
@SuppressWarnings("serial")
public class Run extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IRun{

	IRI newInstance;
	public Run(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Run"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IRun> getAllRunsObjectsCreated(){
		Set<IRun> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Run")).subjects().stream()
		.map(mapper->(IRun)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}