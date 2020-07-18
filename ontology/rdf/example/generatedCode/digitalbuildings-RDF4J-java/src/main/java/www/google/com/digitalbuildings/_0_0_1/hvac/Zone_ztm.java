package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Zone_ztm 
* Zone with only temperature monitoring.
*/
@SuppressWarnings("serial")
public class Zone_ztm extends www.google.com.digitalbuildings._0_0_1.hvac.Ztm implements IZone_ztm{

	IRI newInstance;
	public Zone_ztm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Zone_ztm"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IZone_ztm> getAllZone_ztmsObjectsCreated(){
		Set<IZone_ztm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Zone_ztm")).subjects().stream()
		.map(mapper->(IZone_ztm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}